import pandas as pd
import matplotlib.pyplot as plt


class ChartPlotter:

    def __init__(self, ds_name, results):
        self._results = pd.DataFrame(results)[1]
        self._ds_name = ds_name

    def create_chart(self):
        unique = self._results.unique()
        unique.sort()
        unique_num = len(unique)
        unique = list(unique)
        supports = [i for i in range(1, unique_num+1)]
        quantity = [0 for _ in range(unique_num)]

        for supp in self._results:
            index = unique.index(supp)
            quantity[index] += 1

        plt.clf()
        plt.bar(x=supports, height=quantity, tick_label=unique)

        for i in range(len(quantity)):
            plt.annotate(str(quantity[i]), xy=(supports[i], quantity[i]), ha='center', va='bottom')

        plt.title("Number of frequent itemsets for DS: " + self._ds_name + " (with minimal support: " + str(unique[0]) + ")")
        plt.xlabel("Support")
        plt.ylabel("Number of frequent itemsets")
        plt.savefig(f"results/{self._ds_name}_support.png", format="PNG")
        plt.show()
