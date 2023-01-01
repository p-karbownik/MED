from .readBitDataset import BitDataSet
from bitarray import bitarray
from bitarray import frozenbitarray


class FrequentSet:
    def __init__(self, items: frozenbitarray, diff_set, support, decode):
        self.support = support
        self.items = items
        self.diff_set = diff_set
        self.decode_dict = decode

    def __str__(self):
        items = ""
        for i in range(len(self.items)):
            if self.items[i]:
                items += self.decode_dict[i]
                items += ' '
        return items + " | " + str(self.support)

    def __eq__(self, other):
        if not isinstance(other, FrequentSet):
            return NotImplemented

        return self.items == other.items

    def __hash__(self):
        return hash(self.items)


class BitDECLATRunner:

    def __init__(self, dataset: BitDataSet, minimal_support: int):
        self.dataset = dataset
        self.minimal_support = minimal_support
        self.elements_diff_set_dict = dict()

    def run(self):
        self._prepare_dict()
        first_rules = self._first_step()
        return first_rules.union(self._do_declat(first_rules, self._find_classes(first_rules)))

    def _prepare_dict(self):
        for e in self.dataset.elements:
            self.elements_diff_set_dict[e] = self._calculate_bit_diff_set(self.dataset.encode_dict[e])

    def _calculate_bit_diff_set(self, bit_num):
        tweets_amount = len(self.dataset.transactions)
        bit_diff_set = tweets_amount * bitarray('1')
        transactions = self.dataset.transactions

        for transaction_id in transactions:
            transaction = transactions[transaction_id]
            if transaction[bit_num]:
                bit_diff_set[transaction_id] = False

        return bit_diff_set

    def _first_step(self):
        frequent_items = set()
        elements = self.dataset.elements
        transactions_amount = len(self.dataset.transactions)

        for e in elements:
            support = transactions_amount - self._count_elements_in_array_by_key(e)
            if support >= self.minimal_support:
                encoded_element = len(self.dataset.elements) * bitarray('0')
                encoded_element[self.dataset.encode_dict[e]] = True
                frequent_items.add(
                    FrequentSet(frozenbitarray(encoded_element), self.elements_diff_set_dict[e], support,
                                self.dataset.decode_dict))

        return frequent_items

    def _count_elements_in_array_by_key(self, key):
        bit_arr = self.elements_diff_set_dict[key]
        return bit_arr.count(1)

    def _do_declat(self, previous_rules, classes):
        new_rules = set()

        for r in previous_rules:
            for c in classes:
                if not r.items[c]:
                    new_rule = bitarray(bitarray.copy(r.items))
                    new_rule[c] = True
                    diff_set = self._calculate_diffset(r.diff_set,
                                                       self.elements_diff_set_dict.get(self.dataset.decode_dict[c]))
                    support = len(self.dataset.transactions) - diff_set.count(1)
                    if support >= self.minimal_support:
                        new_rules.add(
                            FrequentSet(frozenbitarray(new_rule), diff_set, support, self.dataset.decode_dict))

        if len(new_rules) != 0:
            return new_rules.union(self._do_declat(new_rules, self._find_classes(new_rules)))
        else:
            return set()

    @staticmethod
    def _find_classes(rules):
        classes = set()

        for r in rules:
            for i in range(len(r.items)):
                if r.items[i]:
                    classes.add(i)

        return classes

    @staticmethod
    def _calculate_diffset(diff_set, element):
        return element | diff_set


def decode(result, show_results: bool):
    if show_results:
        print("Frequent items set | Support")
    decoded = []
    for item in result:
        if show_results:
            print(str(item))
        decoded.append([str(item), item.support])
    return decoded


def get_support_values_list(results):
    support_set = set()

    for result in results:
        support_set.add(result.support)

    return support_set


def get_max_support_value(results):
    return max(get_support_values_list(results))
