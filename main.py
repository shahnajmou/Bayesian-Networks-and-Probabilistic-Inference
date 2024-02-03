from GibbsSampling import GibbsSampling
from Import import importNetwork
from varElim import VariableElimination


class Main:
    def main(self):
        print('FETCHING ALARM NETWORK: \n')
        getnet = importNetwork().read('alarm.bif')
        x = ['HYPOVOLEMIA', 'LVFAILURE', 'ERRLOWOUTPUT']

        print('No Evidence\n')
        e = {}

        print('Gibbs Sampling\n')
        alarm_ne = GibbsSampling().gibbs(X=x, e=e, bnet=getnet, n=400, demo_flag=False)
        print('Approximate probabilities for ' + str(x) + ', given known evidence: ' + str(e))
        print(str(alarm_ne))
        print()

        print('Variable Elimination\n')
        for X in x:
            print('Exact probabilities for ' + X + ', given known evidence ' + str(e))
            factor = VariableElimination().elimination(X, e, getnet)
            print(factor.cpt)
            print()

        print('Little Evidence\n')
        e = {"HRBP": "HIGH", "CO": "LOW", "BP": "HIGH"}

        print('Gibbs Sampling\n')
        alarm_le = GibbsSampling().gibbs(X=x, e=e, bnet=getnet, n=400, demo_flag=False)
        print('Approximate probabilities for ' + str(x) + ', given known evidence: ' + str(e))
        print(str(alarm_le))
        print()

        print('Variable Elimination\n')
        for X in x:
            print('Exact probabilities for ' + X + ', given known evidence ' + str(e))
            factor = VariableElimination().elimination(X, e, getnet)
            print(factor.cpt)
            print()

        print('Moderate evidence\n')
        e = {"HRBP": "HIGH", "CO": "LOW", "BP": "HIGH", 'HRSAT': 'LOW', 'HREKG': 'LOW'}

        print('Gibbs Sampling\n')
        alarm_me = GibbsSampling().gibbs(X=x, e=e, bnet=getnet, n=400, demo_flag=False)
        print('Approximate probabilities for ' + str(x) + ', given known evidence: ' + str(e))
        print(str(alarm_me))
        print()

        print('Variable Elimination\n')
        for X in x:
            print('Exact probabilities for ' + X + ', given known evidence ' + str(e))
            factor = VariableElimination().elimination(X, e, getnet)
            print(factor.cpt)
            print()

        print('FETCHING CHILD NETWORK: \n')
        getnet = importNetwork().read('child.bif')
        x = ['Disease']

        print('No Evidence\n')
        e = {}

        print('Gibbs Sampling\n')
        child_ne = GibbsSampling().gibbs(X=x, e=e, bnet=getnet, n=1000, demo_flag=False)
        print('Approximate probabilities for ' + str(x) + ', given known evidence: ' + str(e))
        print(str(child_ne))
        print()

        print('Variable Elimination\n')
        for X in x:
            print('Exact probabilities for ' + X + ', given known evidence ' + str(e))
            factor = VariableElimination().elimination(X, e, getnet)
            print(factor.cpt)
            print()

        print('Little Evidence\n')
        e = {'LowerBodyO2': '<5', 'RUQO2': '>=12', 'CO2Report': '>=7.5', 'XrayReport': 'Asy/Patchy'}

        print('Gibbs Sampling\n')
        child_le = GibbsSampling().gibbs(X=x, e=e, bnet=getnet, n=1000, demo_flag=False)
        print('Approximate probabilities for ' + str(x) + ', given known evidence: ' + str(e))
        print(str(child_le))
        print()

        print('Variable Elimination\n')
        for X in x:
            print('Exact probabilities for ' + X + ', given known evidence ' + str(e))
            factor = VariableElimination().elimination(X, e, getnet)
            print(factor.cpt)
            print()

        print('Moderate evidence\n')
        e = {'LowerBodyO2': '<5', 'RUQO2': '>=12', 'CO2Report': '>=7.5', 'XrayReport': 'Asy/Patchy',
             'GruntingReport': 'yes', 'LVHReport': 'yes', 'Age': '11-30_days'}

        print('Gibbs Sampling\n')
        child_me = GibbsSampling().gibbs(X=x, e=e, bnet=getnet, n=1000, demo_flag=False)
        print('Approximate probabilities for ' + str(x) + ', given known evidence: ' + str(e))
        print(str(child_me))

        print('Variable Elimination\n')
        for X in x:
            print('Exact probabilities for ' + X + ', given known evidence ' + str(e))
            factor = VariableElimination().elimination(X, e, getnet)
            print(factor.cpt)
            print()

        print('FETCHING HAILFINDER NETWORK: \n')
        getnet = importNetwork().read('hailfinder.bif')
        x = ['SatContMoist', 'LLIW']

        print('No Evidence\n')
        e = {}

        print('Gibbs Sampling\n')
        hailfinder_ne = GibbsSampling().gibbs(X=x, e=e, bnet=getnet, n=1000, demo_flag=False)
        print('Approximate probabilities for ' + str(x) + ', given known evidence: ' + str(e))
        print(str(hailfinder_ne))
        print()

        # print('Variable Elimination\n')
        # for X in x:
        #     print('Exact probabilities for ' + X + ', given known evidence ' + str(e))
        #     factor = VariableElimination().elimination(X, e, getnet)
        #     print(factor.cpt)
        #     print()

        print('Little Evidence\n')
        e = {'RSFest': 'XNIL', 'N32StarFest': 'XNIL', 'MountainFest': 'XNIL', 'AreaMoDryAir': 'VeryWet'}

        print('Gibbs Sampling\n')
        hailfinder_le = GibbsSampling().gibbs(X=x, e=e, bnet=getnet, n=1000, demo_flag=False)
        print('Approximate probabilities for ' + str(x) + ', given known evidence: ' + str(e))
        print(str(hailfinder_le))
        print()

        # print('Variable Elimination\n')
        # for X in x:
        #     print('Exact probabilities for ' + X + ', given known evidence ' + str(e))
        #     factor = VariableElimination().elimination(X, e, getnet)
        #     print(factor.cpt)
        #     print()

        print('Moderate evidence\n')
        e = {'RSFest': 'XNIL', 'N32StarFest': 'XNIL', 'MountainFest': 'XNIL', 'AreaMoDryAir': 'VeryWet',
             'CombVerMo': 'Down', 'AreaMeso_ALS': 'Down', 'CurPropConv': 'Strong'}

        print('Gibbs Sampling\n')
        hailfinder_me = GibbsSampling().gibbs(X=x, e=e, bnet=getnet, n=1000, demo_flag=False)
        print('Approximate probabilities for ' + str(x) + ', given known evidence: ' + str(e))
        print(str(hailfinder_me))

        # print('Variable Elimination\n')
        # for X in x:
        #     print('Exact probabilities for ' + X + ', given known evidence ' + str(e))
        #     factor = VariableElimination().elimination(X, e, getnet)
        #     print(factor.cpt)
        #     print()

        print('\nFETCHING INSURANCE NETWORK: \n')
        getnet = importNetwork().read('insurance.bif')
        x = ['MedCost', 'ILiCost', 'PropCost']

        print('No Evidence\n')
        e = {}

        print('Gibbs Sampling\n')
        insurance_ne = GibbsSampling().gibbs(X=x, e=e, bnet=getnet, n=1000, demo_flag=False)
        print('Approximate probabilities for ' + str(x) + ', given known evidence: ' + str(e))
        print(str(insurance_ne))
        print()

        # print('Variable Elimination\n')
        # for X in x:
        #     print('Exact probabilities for ' + X + ', given known evidence ' + str(e))
        #     factor = VariableElimination().elimination(X, e, getnet)
        #     print(factor.cpt)
        #     print()

        print('Little Evidence\n')
        e = {'Age': 'Adolescent', 'GoodStudent': 'False', 'SeniorTrain': 'False', 'DrivQuality': 'Poor'}

        print('Gibbs Sampling\n')
        insurance_le = GibbsSampling().gibbs(X=x, e=e, bnet=getnet, n=1000, demo_flag=False)
        print('Approximate probabilities for ' + str(x) + ', given known evidence: ' + str(e))
        print(str(insurance_le))
        print()

        # print('Variable Elimination\n')
        # for X in x:
        #     print('Exact probabilities for ' + X + ', given known evidence ' + str(e))
        #     factor = VariableElimination().elimination(X, e, getnet)
        #     print(factor.cpt)
        #     print()

        print('Moderate evidence\n')
        e = {'Age': 'Adolescent', 'GoodStudent': 'False', 'SeniorTrain': 'False', 'DrivQuality': 'Poor',
             'MakeModel': 'Luxury', 'CarValue': 'FiftyThou', 'DrivHistory': 'Zero'}

        print('Gibbs Sampling\n')
        insurance_me = GibbsSampling().gibbs(X=x, e=e, bnet=getnet, n=1000, demo_flag=False)
        print('Approximate probabilities for ' + str(x) + ', given known evidence: ' + str(e))
        print(str(insurance_me))

        # print('Variable Elimination\n')
        # for X in x:
        #     print('Exact probabilities for ' + X + ', given known evidence ' + str(e))
        #     factor = VariableElimination().elimination(X, e, getnet)
        #     print(factor.cpt)
        #     print()

        print('\nFETCHING WIN95 NETWORK: \n')
        getnet = importNetwork().read('win95pts.bif')
        x = ['Problem1', 'Problem2', 'Problem3', 'Problem4', 'Problem5', 'Problem6']

        print('No Evidence\n')
        e = {}

        print('Gibbs Sampling\n')
        win95_ne = GibbsSampling().gibbs(X=x, e=e, bnet=getnet, n=1000, demo_flag=False)
        print(str(win95_ne))
        print()

        # print('Variable Elimination\n')
        # for X in x:
        #     print('Exact probabilities for ' + X + ', given known evidence ' + str(e))
        #     factor = VariableElimination().elimination(X, e, getnet)
        #     print(factor.cpt)
        #     print()

        print('Problem 1\n')
        e = {'Problem1': 'No_Output'}

        print('Gibbs Sampling\n')
        win95_1 = GibbsSampling().gibbs(X=x, e=e, bnet=getnet, n=1000, demo_flag=False)
        print(str(win95_1))
        print()

        # print('Variable Elimination\n')
        # for X in x:
        #     print('Exact probabilities for ' + X + ', given known evidence ' + str(e))
        #     factor = VariableElimination().elimination(X, e, getnet)
        #     print(factor.cpt)
        #     print()

        print('Problem 2\n')
        e = {'Problem2': 'Too_Long'}

        print('Gibbs Sampling\n')
        win95_2 = GibbsSampling().gibbs(X=x, e=e, bnet=getnet, n=1000, demo_flag=False)
        print(str(win95_2))
        print()

        # print('Variable Elimination\n')
        # for X in x:
        #     print('Exact probabilities for ' + X + ', given known evidence ' + str(e))
        #     factor = VariableElimination().elimination(X, e, getnet)
        #     print(factor.cpt)
        #     print()

        print('Problem 3\n')
        e = {'Problem3': 'No'}

        print('Gibbs Sampling\n')
        win95_3 = GibbsSampling().gibbs(X=x, e=e, bnet=getnet, n=1000, demo_flag=False)
        print(str(win95_3))
        print()

        # print('Variable Elimination\n')
        # for X in x:
        #     print('Exact probabilities for ' + X + ', given known evidence ' + str(e))
        #     factor = VariableElimination().elimination(X, e, getnet)
        #     print(factor.cpt)
        #     print()

        print('Problem 4\n')
        e = {'Problem4': 'No'}

        print('Gibbs Sampling\n')
        win95_4 = GibbsSampling().gibbs(X=x, e=e, bnet=getnet, n=1000, demo_flag=False)
        print(str(win95_4))
        print()

        # print('Variable Elimination\n')
        # for X in x:
        #     print('Exact probabilities for ' + X + ', given known evidence ' + str(e))
        #     factor = VariableElimination().elimination(X, e, getnet)
        #     print(factor.cpt)
        #     print()

        print('Problem 5\n')
        e = {'Problem5': 'No'}

        print('Gibbs Sampling\n')
        win95_5 = GibbsSampling().gibbs(X=x, e=e, bnet=getnet, n=1000, demo_flag=False)
        print(str(win95_5))
        print()

        # print('Variable Elimination\n')
        # for X in x:
        #     print('Exact probabilities for ' + X + ', given known evidence ' + str(e))
        #     factor = VariableElimination().elimination(X, e, getnet)
        #     print(factor.cpt)
        #     print()

        print('Problem 6\n')
        e = {'Problem6': 'Yes'}

        print('Gibbs Sampling\n')
        win95_6 = GibbsSampling().gibbs(X=x, e=e, bnet=getnet, n=1000, demo_flag=False)
        print('Approximate probabilities for ' + str(x) + ', given known evidence: ' + str(e))
        print(str(win95_6))
        print()

        # print('Variable Elimination\n')
        # for X in x:
        #     print('Exact probabilities for ' + X + ', given known evidence ' + str(e))
        #     factor = VariableElimination().elimination(X, e, getnet)
        #     print(factor.cpt)
        #     print()


if __name__ == "__main__":
    Main().main()
