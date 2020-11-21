def MakeDecision(ask):
  if ask == 0:
    return "No lets stay the course"
    ask+1
  if ask == 1:
    return "Let me think about it"
    ask+1
  if ask == 2:
    return "Thats right, you should do that, good idea"
  return "Victory"
print(MakeDecision(2))