import sqlite3


def apply_job():
    conn = sqlite3.connect("job.db")
    cur = conn.cursor()

    name = input("Enter name: ")
    exp = int(input("Enter experience: "))

    
    cur.execute("select skill_name from skills")
    skills = cur.fetchall()

    print("\nAvailable skills are:")
    count = 1
    for s in skills:
        print(count, ")", s[0])
        count += 1

    choice = int(input("Choose skill number: "))
    chosen_skill = skills[choice-1][0]

    
    cur.execute("insert into applicant values(?,?,?)", (name, exp, chosen_skill))

    conn.commit()
    conn.close()

    print("Applied successfully\n")



def recruit_people():
    conn = sqlite3.connect("job.db")
    cur = conn.cursor()

    
    cur.execute("select skill_name from skills")
    skills = cur.fetchall()

    print("\nSelect skill required:")
    for i in range(len(skills)):
        print(i+1, "-", skills[i][0])

    ch = int(input("Enter option: "))
    req_skill = skills[ch-1][0]

    min_exp = int(input("Enter minimum experience: "))

    
    cur.execute("update skills set search_count = search_count+1 where skill_name=?", (req_skill,))

    
    cur.execute("select * from applicant where skill=? and years_of_experience>=?", (req_skill, min_exp))
    result = cur.fetchall()

    print("\nEligible candidates:")
    if result == []:
        print("No candidates found")
    else:
        for r in result:
            print("Name:", r[0], "| Exp:", r[1])

    conn.commit()
    conn.close()
    print()



def check_trend():
    conn = sqlite3.connect("job.db")
    cur = conn.cursor()

    cur.execute("select * from skills order by search_count desc limit 5")
    data = cur.fetchall()

    print("\nTop skills currently:")
    for d in data:
        print(d[0], "-", d[1])

    conn.close()
    print()



while True:
    print("====== MENU ======")
    print("1. Apply")
    print("2. Recruit")
    print("3. Trends")
    print("4. Exit")

    opt = input("Enter choice: ")

    if opt == "1":
        apply_job()

    elif opt == "2":
        recruit_people()

    elif opt == "3":
        check_trend()

    elif opt == "4":
        print("Exiting...")
        break

    else:
        print("Wrong input\n")
