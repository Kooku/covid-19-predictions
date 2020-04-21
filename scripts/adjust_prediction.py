import itertools

def calc_weight(num):
    return (1001-num) / 100000

def calc_accuracy(prediction, print_values=False):
    actual = [1469, 2088, 2790, 3251, 4042, 4682, 5576, 6280, 7398, 8527, 9560, 11284, 12437, 12978, 15756, 16563, 17872, 19141, 20654, 22059, 23316, 24298, 25679, 27034, 28208, 30808, 32813, 34355]
    delta = [340.6661140000001, 167.75270200000023, 16.712113000000045, 114.82030600000007, 6.138746000000083, 102.8047459999998, 36.88873500000045, 239.19654400000036, 103.69540700000016, 30.30747800000063, 122.00756200000069, 413.0587400000004, 318.4429199999995, 440.74631000000045, 991.0149600000004, 412.5266100000008, 303.73219999999856, 129.59659000000102, 180.9960600000013, 112.62207000000126, 109.10023000000001, 605.0789399999994, 695.6079700000009, 800.4060099999988, 1069.6430900000014, 108.04416000000128, 715.5471499999985, 888.2883999999976]
    count = 0
    for x,y,d in zip(actual, prediction, delta):
        if abs(x-y) < d:
            if print_values:
                print('Better value: {}'.format(y))
            count += 1

    # print('Count: {}, Percentage: {}'.format(count, count/len(actual)))
    return count, count/len(actual)

sign = [1001, 1001, 1001, 1001, 348, 45, 32, 91, 165, 49, 41, 62, 36, 91, 53, 77, 55, 84, 71, 104, 48, 59, 81, 81, 119, 90, 169, 84, 121, 90, 137, 248, 203, 228, 258]
stay = [48, 62, 46, 27, 31, 40, 34, 25, 13, 8, 2, 2, 3, 6, 6, 8, 6, 5, 5, 5, 5, 6, 6, 6, 6, 11, 9, 10, 48, 8, 7, 21, 26, 15, 22]
herd = [157, 933, 802, 557, 452, 310, 1001, 1001, 1001, 1001, 754, 948, 1001, 1001, 1001, 301, 554, 597, 658, 785, 391, 745, 655, 303, 319, 286, 362, 202, 213, 120, 165, 185, 227, 319, 332]
contact = [1001, 1001, 1001, 1001, 1001, 1001, 1001, 1001, 1001, 1001, 1001, 1001, 1001, 1001, 1001, 1001, 1001, 1001, 925, 1001, 889, 704, 1001, 1001, 1001, 695, 1001, 697, 621, 49, 68, 196, 212, 208, 232]

predict = [1809.666114, 2255.752702, 2773.287887, 3365.820306, 4035.861254, 4784.804746, 5612.888735, 6519.196544, 7501.695407, 8557.307478, 9682.007562, 10870.94126, 12118.55708, 13418.74631, 14764.98504, 16150.47339, 17568.2678, 19011.40341, 20473.00394, 21946.37793, 23425.10023, 24903.07894, 26374.60797, 27834.40601, 29277.64309, 30699.95584, 32097.45285, 33466.7116, 34804.76820726625, 36109.10137742164, 37377.61184645985, 38608.59832212259, 39800.73100866787, 40953.02356439783, 42064.804249323315, 43135.686896631574, 44165.54222942782, 45154.469941364136, 46102.77186732711, 47010.92648874634, 47879.564947249855, 48709.44867995164, 49501.448738919404]

sign_avg = sum(sign[10:]) / len(sign[10:])
stay_avg = sum(stay[10:]) / len(stay[10:])
herd_avg = sum(herd[10:]) / len(herd[10:])
contact_avg = sum(contact[10:]) / len(contact[10:])

nums = [1,2,3,4,5]
adjustment_records = []
for a,b,c,d in itertools.product(range(1,6),repeat=4):
    # print('a: {}, b: {}, c: {}, d: {}'.format(a,b,c,d))
    adjustments = []
    for si, st, he, co, pr in zip(sign, stay, herd, contact, predict):
        multiplier = 1 - a*calc_weight(si) - b*calc_weight(st) + c*calc_weight(he) - d*calc_weight(co)
        adjustments.append(pr*multiplier)
        if (a == 1 and b == 1 and c == 5 and d == 4):
            print(pr*multiplier)
    if (a == 1 and b == 1 and c == 5 and d == 4):
        count, percentage = calc_accuracy(adjustments, print_values=True)
    else:
        count, percentage = calc_accuracy(adjustments)
    adjustment_records.append(((a,b,c,d), percentage))

adjustment_records.sort(key=lambda x:x[1], reverse=True)
for item in adjustment_records[:10]:
    print('a,b,c,d: {}, improvement percentage: {}%'.format(item[0], item[1]*100))

multiplier = 1 - calc_weight(sign_avg)*10 - calc_weight(stay_avg)*10 + 50*calc_weight(herd_avg) - 40*calc_weight(contact_avg)
print(multiplier)
