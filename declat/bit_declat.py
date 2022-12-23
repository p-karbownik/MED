from readDataset import DataSet
from bitarray import bitarray
from declat import FrequentSet


class BitDECLATRunner:

    def __init__(self, dataset: DataSet, minimal_support: int):
        self.dataset = dataset
        self.minimal_support = minimal_support
        self.elements_dict = dict()

    def run(self):
        self._prepare_dict()
        first_rules = self._first_step()
        return first_rules.union(self._do_declat(first_rules, self._find_classes(first_rules)))

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
            if transactions_amount - self._count_elements_in_array(e) >= self.minimal_support:
                frequent_items.add(FrequentSet(frozenset({e}), self.elements_dict[e]))

        return frequent_items

    def _count_elements_in_array(self, key):
        bit_arr = self.elements_dict[key]
        sum_of_bits = 0
        for bit in bit_arr:
            sum_of_bits += int(bit)
        return sum_of_bits

    def _do_declat(self, first_rules, classes):
        pass

    def _find_classes(self, first_rules):
        pass
