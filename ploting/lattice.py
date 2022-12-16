import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.pyplot import text


class LatticePlotter:
    def __init__(self, decoded_results, name, support):
        self._name = name
        self._support = support
        self._results = decoded_results
        self._from_node = []
        self._to_node = []
        self._levels_capacity = [1]
        self._levels = [["{}"]]

    def plot_lattice(self):
        max_level = self._find_max_tags_num()

        previous_level = self._create_first_level()
        for i in range(2, max_level + 1):
            previous_level = self._create_next_level(i, previous_level)
        
        self._create_graph()

    def _find_max_tags_num(self):
        max_tags = 0
        for record in self._results:
            tags = record[0].count("#")
            if tags > max_tags:
                max_tags = tags
        return max_tags

    def _create_first_level(self):
        first_level = []
        records_to_delete = []

        for record in self._results:
            if record[0].count("#") == 1:
                self._from_node.append("{}")  # lowest level
                self._to_node.append(record[0])
                first_level.append(record[0])
                records_to_delete.append(record)

        for record_to_delete in records_to_delete:
            self._results.remove(record_to_delete)

        self._levels_capacity.append(len(first_level))
        self._levels.append(first_level)

        return first_level

    def _create_next_level(self, current_level_num, previous_level):
        current_level = []
        records_to_delete = []

        for record in self._results:
            tags_num = record[0].count("#")
            if tags_num == current_level_num:
                current_level.append(record[0])
                records_to_delete.append(record)

        for record_to_delete in records_to_delete:
            self._results.remove(record_to_delete)

        self._levels_capacity.append(len(current_level))
        self._levels.append(current_level)

        for current_tags in current_level:
            for prev_tags in previous_level:
                previous_in_current = 0
                tags = prev_tags.split(" ")

                for p_tag in tags:
                    if p_tag in current_tags:
                        previous_in_current += 1

                if previous_in_current == current_level_num - 1:
                    self._from_node.append(prev_tags)
                    self._to_node.append(current_tags)

        return current_level

    def _create_graph(self):
        g = nx.Graph()

        max_nodes_in_single_level = max(self._levels_capacity)

        level = 0
        node_num = 0
        legend = {}
        for nodes, nodes_num in zip(self._levels, self._levels_capacity):
            starting_x = max_nodes_in_single_level / (nodes_num+1)
            for i in range(len(nodes)):
                x = starting_x * (i+1)
                # g.add_node(i, pos=(x, level))
                g.add_node(nodes[i], pos=(x, level))
                legend.update({nodes[i]: node_num})
                node_num += 1
            level += 1

        for from_n, to_n in zip(self._from_node, self._to_node):
            g.add_edge(from_n, to_n)
            # g.add_edge(legend.get(from_n), legend.get(to_n))

        pos = nx.get_node_attributes(g, 'pos')
        lay = nx.spring_layout(g)

        for node, _ in lay.items():
            coords = pos.get(node)
            text(coords[0], coords[1], node, fontsize=6, ha='center', va='center')

        plt.title(f"Lattice for DS: {self._name} with Min Supp: {self._support}")

        nx.draw(g, pos=pos, with_labels=False, font_size=11)
        # we can show or save graph, not both
        # plt.show(block=False)
        plt.rcParams.update({'font.size': 9})
        plt.savefig(f"results/{self._name}.png", format="PNG")

        # df = pd.DataFrame.from_dict(legend.items()).set_index(1)
        # df.to_csv(f"results/{self._name}.csv", header=False)
