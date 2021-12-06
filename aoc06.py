# state = [3,4,3,1,2]
state = [3,4,3,1,2,1,5,1,1,1,1,4,1,2,1,1,2,1,1,1,3,4,4,4,1,3,2,1,3,4,1,1,3,4,2,5,5,3,3,3,5,1,4,1,2,3,1,1,1,4,1,4,1,5,3,3,1,4,1,5,1,2,2,1,1,5,5,2,5,1,1,1,1,3,1,4,1,1,1,4,1,1,1,5,2,3,5,3,4,1,1,1,1,1,2,2,1,1,1,1,1,1,5,5,1,3,3,1,2,1,3,1,5,1,1,4,1,1,2,4,1,5,1,1,3,3,3,4,2,4,1,1,5,1,1,1,1,4,4,1,1,1,3,1,1,2,1,3,1,1,1,1,5,3,3,2,2,1,4,3,3,2,1,3,3,1,2,5,1,3,5,2,2,1,1,1,1,5,1,2,1,1,3,5,4,2,3,1,1,1,4,1,3,2,1,5,4,5,1,4,5,1,3,3,5,1,2,1,1,3,3,1,5,3,1,1,1,3,2,5,5,1,1,4,2,1,2,1,1,5,5,1,4,1,1,3,1,5,2,5,3,1,5,2,2,1,1,5,1,5,1,2,1,3,1,1,1,2,3,2,1,4,1,1,1,1,5,4,1,4,5,1,4,3,4,1,1,1,1,2,5,4,1,1,3,1,2,1,1,2,1,1,1,2,1,1,1,1,1,4]

no_of_days = 256

def day(state: list):
    count = state.count(0)
    state = [x for x in state if x != 0]

    for i in range(len(state)):
        state[i] -= 1

    state += [6] * count + [8] * count
    # print(state)
    return

# for _ in range(no_of_days):
#     day(state)
# # print(state)
# print(f"no. of fish after {no_of_days}days= {len(state)}")

def state_dct(state: list) -> dict:
    state_dct = {}
    for i in range(9):
        state_dct[i] = state.count(i)
    # print(state_dct)
    return state_dct

def day_dct(state: dict):
    count = state[0]

    for i in range(8):
        state[i] = state[i +1]
    
    state[6] += count
    state[8] = count
    return

state_d = state_dct(state)
for _ in range(no_of_days):
    day_dct(state_d)
print(f"no. of fish after {no_of_days}days= {sum(state_d.values())}")
