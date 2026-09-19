instrument = "MES"
entry_price = 6120
stop_price = 6115
target_price = 6130

risk = abs(entry_price - stop_price)
reward = abs(target_price - entry_price)
risk_reward = reward / risk

print("instrument:", instrument)
print("Risk:", risk)
print("Reward:", reward)
print("R:R:", risk_reward)


