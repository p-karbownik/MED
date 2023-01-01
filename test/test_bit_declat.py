from declat.readBitDataset import read_bit_data_set
from declat.bit_declat import BitDECLATRunner
from bitarray import frozenbitarray


def test():
    expected_result = {frozenbitarray('100000'), frozenbitarray('010000'), frozenbitarray('001000'),
                       frozenbitarray('000100'), frozenbitarray('000010'), frozenbitarray('000001'),
                       frozenbitarray('110000'), frozenbitarray('101000'), frozenbitarray('100100'),
                       frozenbitarray('100010'), frozenbitarray('100001'), frozenbitarray('011000'),
                       frozenbitarray('010100'), frozenbitarray('010010'), frozenbitarray('001100'),
                       frozenbitarray('001010'), frozenbitarray('001001'), frozenbitarray('000110'),
                       frozenbitarray('111000'), frozenbitarray('110100'), frozenbitarray('101100'),
                       frozenbitarray('101010'), frozenbitarray('101001'), frozenbitarray('011100'),
                       frozenbitarray('010110'), frozenbitarray('111100')}

    ds = read_bit_data_set("../dataset/test2.csv")
    bdr = BitDECLATRunner(ds, 2)
    run_result = bdr.run()
    result = set()

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
