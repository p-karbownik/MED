from readDataset import DataSet


class FrequentSet:
    def __init__(self, items: frozenset, diff_set):
        self.items = items
        self.diff_set = diff_set

    def __str__(self):
        return ' '.join(self.items)

    def __eq__(self, other):
        if not isinstance(other, FrequentSet):
            return NotImplemented

        return self.items == other.items

    def __hash__(self):
        return hash(self.items)

    def get_diff_length(self):
        return len(self.diff_set)

    def calculate_support(self, transactions_number):
        return transactions_number - len(self.items)


class DECLATRunner:

    def __init__(self):
        self.dataset = None
        self.minimal_support = None
        self.elements_dict = dict()

    def prepare_element_dict(self, elements, transactions):
        for e in elements:
            self.elements_dict[e] = calculate_diff_set({e}, transactions)

    def first_step(self, elements, transactions_length):
        frequent_items = set()

        for e in elements:
            if transactions_length - len(self.elements_dict[e]) >= self.minimal_support:
                frequent_items.add(FrequentSet(frozenset({e}), self.elements_dict[e]))

        return frequent_items

    def find_classes(self, rules):
        classes = set()

        for r in rules:
            classes.update(r.items)

        return classes

    def do_declat(self, rules_from_previous_step, classes):
        new_rules = set()

        for r in rules_from_previous_step:
            for c in classes:
                if not r.items.__contains__(c):
                    new_rule = r.items.union({c})
                    diff_set = calculate_diff_set(new_rule, self.dataset.transactions)
                    if len(self.dataset.transactions) - len(diff_set) >= self.minimal_support:
                        new_rules.add(FrequentSet(new_rule, diff_set))

        if len(new_rules) != 0:
            return new_rules.union(self.do_declat(new_rules, self.find_classes(new_rules)))
        else:
            return set()

    def run(self, dataset: DataSet, minimal_support):
        self.dataset = dataset
        self.minimal_support = minimal_support
        self.prepare_element_dict(dataset.elements, dataset.transactions)
        first_rules = self.first_step(dataset.elements, len(dataset.transactions))
        result = first_rules.union(self.do_declat(first_rules, self.find_classes(first_rules)))
        return result


def decode_result(result, transactions_number):
    print("Rule | Support")
    for item in result:
        print(str(item) + ' | ' + str(item.calculate_support(transactions_number)))


def calculate_diff_set(rule: set, transactions: dict):
    diff_set = set()

    for transaction_id in range(0, len(transactions)):
        if len(transactions[transaction_id].intersection(rule)) != len(rule):
            diff_set = diff_set.union({transaction_id})

    return diff_set
