from Code.Pos_Neg_Zero import positive_negative_zero

assert positive_negative_zero(10) == "Positive"
print("Test Case 1 pass")
assert positive_negative_zero(-5) == "Negative"
print("Test Case 1 pass")
assert positive_negative_zero(0) == "zero"
print("Test Case 1 pass")
assert positive_negative_zero(25) == "Positive"
print("Test Case 1 pass")
assert positive_negative_zero(100) == "Positive"
print("Test Case 1 pass")