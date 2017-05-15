# Chapter 3: Growth of Functions

**Asymptotic** efficiency of algorithms: How running time of an algoirthm increase with the size of the input.

**Asymptote** - a line that continually approaches a given curve but does not meet it at any finite distance.


## Asymptotic Notation

Describers the asymptotic running time of an algorithm in terms of **functions**.  

Asymptotic notation can be used to characterize running time, space, or other aspects of algorithms. Also, it can be used to characterize different types of run times (worse-case, average-case, best-case).

O - notation: Big O notation

- Asymptotic upper bound
- T(n) is 𝜪(f(n)): (Omicron) 
- f(n) describes the upper bound of T(n)
- growth rate of T(n) <= growth rate of f(n)

Ω - notation: Asymptotic lower bound

- Asymptotic lower bound
- T(n) is Ω(f(n)): (Omega) 
- f(n) describes the lower bound of T(n)
- growth rate of T(n) >= growth rate of f(n)

Θ - notation: 

- Asymptotically tight bound
- T(n) is Θ(f(n)): (Theta) 
- f(n) describes the exact bound of T(n)
- growth rate of T(n) == growth rate of f(n)

𝝄 - notation: Little o notation

- T(n) is 𝝄(f(n)): (Omicron) 
- f(n) is the upper bound of T(n) but that T(n) can never be equal to f(n)
- o-notation denotes an upper bound that is **not asymp- totically tight**
- growth rate of T(n) < growth rate of f(n)

**Theorem 3.1**
For any two functions f(n) and g(n), we have f(n) = Θ(g(n)) if and only if f(n) =  O(g(n)) and f(n) =  Ω(g(n)).

###Exercises

**3.1-1**

