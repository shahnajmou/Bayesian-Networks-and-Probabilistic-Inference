import copy
import numpy.random as random
from Network import Network
from Node import Node
class GibbsSampling:
    def __init__(self):
        self.count = 0

    def gibbs(self, X, e, bnet: Network, n, demo_flag):
        samplelist = []
        sample = copy.deepcopy(e)
        frontier = []
        root = []
        for node in bnet.network.values():
            self.count += 1
            if len(node.parents) == 0:
                if node.name not in e:
                    frontier.append(node)
                    root.append(node)
                else:
                    [frontier.append(bnet.network[child]) for child in node.children]
        for node in root:
            self.count += 1
            sample, frontier = self.sample_node(node, bnet, sample, sample, frontier)

        while len(frontier) > 0:
            for node in frontier:
                self.count += 1
                if e.get(node.name) is None:
                    s_flag = True
                    for parent in node.parents:
                        self.count += 1
                        if parent not in sample:
                            s_flag = False
                    if s_flag:
                        sample, frontier = self.sample_node(node, bnet, sample, sample, frontier)
        samplelist.append(sample)

        for i in range(n - 1):
            self.count += 1
            sample = copy.deepcopy(e)
            frontier = []
            root = []
            for node in bnet.network.values():
                self.count += 1
                if len(node.parents) == 0:
                    if node.name not in e:
                        frontier.append(node)
                        root.append(node)
                    else:
                        [frontier.append(bnet.network[child]) for child in node.children]

            for node in root:
                self.count += 1
                sample, frontier = self.sample_node(node, bnet, sample, samplelist[i], frontier)

            while len(frontier) > 0:
                for node in frontier:
                    self.count += 1
                    if e.get(node.name) is None:
                        s_flag = True
                        for parent in node.parents:
                            self.count += 1
                            if parent not in sample:
                                s_flag = False
                        if s_flag:
                            sample, frontier = self.sample_node(node, bnet, sample, samplelist[i], frontier)

            samplelist.append(sample)
        if demo_flag:
            for s in samplelist:
                print(s)

        results = []
        for var in X:
            self.count += 1
            values = []
            for sample in samplelist:
                self.count += 1
                values.append(sample[var])
            dist = []
            for state in bnet.network[var].states:
                self.count += 1
                count = 0
                for val in values:
                    self.count += 1
                    if val == state:
                        count += 1
                dist.append(str(state) + ": " + str(count / n))
            results.append(str(var) + ": " + str(dist))
            print(str(var) + ' count ' + str(self.count))
            self.count = 0
        return results

    def sample_node(self, node: Node, bnet: Network, cur_sample, prev_sample, frontier):
        if len(node.parents) == 0:
            s_val = random.choice(node.states, 1, p=node.probabilities["table"])
        else:
            p_vals = ()
            for parent in node.parents:
                self.count += 1
                p_vals += (prev_sample.get(parent),)
            p = self.normalize_distribution(node, p_vals)
            s_val = random.choice(node.states, 1, p=p)
        cur_sample[node.name] = s_val[0]
        for child in node.children:
            self.count += 1
            if bnet.network[child] not in frontier:
                frontier.append(bnet.network[child])
        frontier.remove(node)
        frontier_nodes = copy.copy(frontier)
        for node in frontier_nodes:
            self.count += 1
            if node.name in cur_sample:
                frontier.remove(node)
        return cur_sample, frontier

    @staticmethod
    def normalize_distribution(node, p_vals):
        denom = sum(float(prob) for prob in node.probabilities[p_vals])
        p = ()
        for prob in node.probabilities[p_vals]:
            p += (float(prob) / denom,)
        return p