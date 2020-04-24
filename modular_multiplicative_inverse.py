# If a no. can be expressed as a fraction P/Q,
# where P and Q are integers (P≥0, Q>0) and Q is coprime with another no. m
# then modular multiplicative inverse is given by P*Q^-1 % m.
# Eg.
# Program to find modular multiplicative inverse
p = 5
q = 16
m = 998244353 
print(p*pow(q,m-2,m)%m)