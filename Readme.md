# Task 1
Observing the sky for a duration of 3 minutes yields a 60% probability of spotting a plane. Your assignment is to calculate and explain the probability of spotting a plane within 1 minute based on this observation. Provide a detailed solution outlining the reasoning behind your calculations.
```
A: Observing a plane in 3 minutes
B: Observing a Plane in 1 minute
P(A) = 0.6
P(Not A) = 1 – P(A) = 1 – 0.6 = 0.4
P(B) = 1 – P(Not B)
```
Also we know that Probability of event b and event c is P(b)*p(c), so we can say Probability of not observing a plane in 3 minutes is probability of not observing a plane in 1 minute to the power of 3 (P(Not B) ^ 3) 

```
P(Not B) ^ 3 = P(Not A) = 0.4 => P(Not B) = 30.4 = 0.736806
P(B) = 1 – P(Not B) = 1 - 0.736806 = 0.263194
```
# Task 2

# Building the model
To setup the environment for building model, you need to run `make dependency`
- It will create a virtual env in .env if not exists
- Source it
- Install requirements

You can find [Model Building Documentation here](IDClassification.ipynb) 

# Running the app
To run app you need to run `docker compose up` it will
- Run frontend on `localhost:3000`
- Run backend on `localhost:8000`


# Testing
To run tests for backend, you can run:
- `python ba