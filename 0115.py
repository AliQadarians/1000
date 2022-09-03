quiz1 = float(input('Enter grade for quiz one: '))
quiz2 = float(input('Enter grade for quiz two: '))
mid = float(input('Enter grade for mid term: '))
final = float(input('Enter grade for final: '))
sum = (quiz1 + quiz2) * 5 * 0.25 + mid * 0.25 + final * 0.5
if sum >= 90 and sum <= 100:
    print('Grade A')
elif sum < 90 and sum >= 80:
    print('Grade B')
elif sum < 80 and sum >= 70:
    print('Grad is C')
elif sum < 70 and sum >= 60:
    print('Grade is D')
elif sum < 60:
    print('Grade is E')
