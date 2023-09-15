student = {
  "Tom": 1,
  "Thomas": 3,
  "Tommy": 2,
  "units": [
    {
      "name": "Web Development",
      "credits": 100,
      "grade": "A"
    },
    {
      "name": "Network and System Administration",
      "credits": 50,
      "grade": "E"
    },
    {
      "name": "Java",
      "credits": 200,
      "grade": "B"
    }
  ],
  "total_credits": 0,
  "GPA": 0
}

grade_weight_mapping = {
  "A": 4,
  "B": 3,
  "C": 2,
  "D": 1,
  "E": 0
}

for g in student["units"]:
  student["total_credits"] += grade_weight_mapping[g["grade"]]
student["GPA"] = format(student["total_credits"] / len(student["units"]), ".2f")
  
print(student["total_credits"])
print(student["GPA"])

guests = ["Harry", "Jack", "Tom", "Patrick", "Valentin", "Justine", "Tom"]

ipt = input("Name: ")
print("Welcome in" if ipt in guests else "get lost!")

print(guests)
guests = list(set(guests))
print(guests)

meetings = [["Monday", "3:30PM", "Joe", "Samantha"], ["Wednesday", "1:15PM", "Sam", "Joe"], ["Sunday", "1:00AM"]]
name = input("Name: ")

mtgs = []
for m in meetings:
  if(name in m[2:]):
    mtgs.append(m)
    
print(mtgs)