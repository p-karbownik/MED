from .readDataset import DataSet
from bitarray import bitarray


class FrequentSet:
    def __init__(self, items: frozenset, diff_set, support):
        self.support = support
        self.items = items
        self.diff_set = diff_set

    def __str__(self):
        items = ' '.join(self.items)
        return items + " | " + str(self.support)

    def __eq__(self, other):
        if not isinstance(other, FrequentSet):
            return NotImplemented

        same_elements = 0

        for i in other.items:
            if self.items.__contains__(i):
                same_elements += 1

        return same_elements == len(self.items)

    def __hash__(self):
        return hash(self.items)


class BitDECLATRunner:

    def __init__(self, dataset: DataSet, minimal_support: int):
        self.dataset = dataset
        self.minimal_support = minimal_support
        self.elements_dict = dict()

    def run(self):
        self._prepare_dict()
        first_rules = self._first_step()
        return first_rules.union(self._do_declat(first_rules))

    def _prepare_dict(self):
        for e in self.dataset.elements:
            self.elements_dict[e] = self._calculate_bit_diff_set({e})

    def _calculate_bit_diff_set(self, rule: set):
        tweets_amount = len(self.dataset.transactions)
        bit_diff_set = tweets_amount * bitarray('0')
        transactions = self.dataset.transactions

        for transaction_id in transactions:
            if len(transactions[transaction_id].intersection(rule)) != len(rule):
                bit_diff_set[transaction_id] = True

        return bit_diff_set

    def _first_step(self):
        frequent_items = set()
        elements = self.dataset.elements
        transactions_amount = len(self.dataset.transactions)

        for e in elements:
            support = transactions_amount - self._count_elements_in_array_by_key(e)
            if support >= self.minimal_support:
                frequent_items.add(FrequentSet(frozenset({e}), self.elements_dict[e], support))

        return frequent_items

    def _count_elements_in_array_by_key(self, key):
        bit_arr = self.elements_dict[key]
        sum_of_bits = 0
        for bit in bit_arr:
            sum_of_bits += int(bit)
        return sum_of_bits

    def _do_declat(self, previous_rules):
        new_rules = set()

        for r1 in previous_rules:
            for r2 in previous_rules:
                if len(r1.items.intersection(r2.items)) == len(r1.items)-1:
                    new_rule = r1.items.union(r2.items)
                    diff_set = self._calculate_diffset(r1.diff_set, r2.diff_set)
                    support = r1.support - self.count_elements_in_array(diff_set)
                    if support >= self.minimal_support:
                        new_rules.add(FrequentSet(new_rule, diff_set, support))

        if len(new_rules) != 0:
            return new_rules.union(self._do_declat(new_rules))
        else:
            return set()

    @staticmethod
    def _find_classes(rules):
        classes = set()

        for r in rules:
            classes.update(r.items)

        return classes

    @staticmethod
    def _calculate_diffset(diff_set, element):
        return element & ~diff_set

    @staticmethod
    def count_elements_in_array(diff_set):
        sum_of_bits = 0
        for bit in diff_set:
            sum_of_bits += int(bit)
        return sum_of_bits


def decode(result, show_results: bool):
    if show_results:
        print("Frequent items set | Support")
    decoded = []
    for item in result:
        if show_results:
            print(str(item))
        decoded.append([str(item), item.support])
    return decoded
