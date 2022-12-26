from declat.readDataset import read_data_set
from declat.bit_declat import BitDECLATRunner, decode


def test():
    expected_result = {frozenset(['a']), frozenset(['b']), frozenset(['c']), frozenset(['e']), frozenset(['f']),
                       frozenset(['h']), frozenset(['a', 'b']), frozenset(['a', 'c']), frozenset(['a', 'e']),
                       frozenset(['a', 'f']), frozenset(['a', 'h']),
                       frozenset(['b', 'c']), frozenset(['b', 'e']), frozenset(['b', 'f']), frozenset(['c', 'e']),
                       frozenset(['c', 'e']),
                       frozenset(['c', 'f']), frozenset(['c', 'h']), frozenset(['e', 'f']),
                       frozenset(['a', 'b', 'c']), frozenset(['a', 'b', 'e']), frozenset(['a', 'c', 'e']),
                       frozenset(['a', 'c', 'f']), frozenset(['a', 'c', 'h']), frozenset(['b', 'c', 'e']),
                       frozenset(['b', 'e', 'f']), frozenset(['a', 'b', 'c', 'e'])
                       }
    ds = read_data_set("../dataset/test2.csv")
    bdr = BitDECLATRunner(ds, 2)
    run_result = bdr.run()
    result = set()

    print(len(expected_result))
    print(len(run_result))

    for r in run_result:
        result.add(r.items)

    if len(result) != len(expected_result):
        print("Test failed - size difference between expected and actual result")
    else:
        if len(result.difference(expected_result)) != 0:
            print("Results are different")
            print("The difference: " + str(result.difference(expected_result)))
        else:
            print("Test passed")


if __name__ == '__main__':
    test()
