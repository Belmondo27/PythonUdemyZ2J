capital = 5000

RateofInterest = 0.08

inflationRate = 0.15

zwrot = capital * RateofInterest

zwrotInfl = capital * inflationRate

print("Zwrot z inwestycji wynosi: ", zwrot)
print("Strata z powodu inflacji wynosi: ", zwrotInfl)


calcapital1 = (capital + zwrot) - zwrotInfl

print("Całkowita kwota kapitału wynosi: ", calcapital1)