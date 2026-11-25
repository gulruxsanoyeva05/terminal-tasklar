GROUPS=[
    {
        "name":"1-24 att",
        "students":[
            {
                "student_name":"ali",
                "davomat":[
                    {  "date":"10:11:2026", "status":"keldi" } ,
                    {  "date":"10:11:2026", "status":"kelmadi" } ,
                    {  "date":"10:11:2026", "status":"keldi" } ,
                    {  "date":"10:11:2026", "status":"keldi" } ,
                 ],

                "baholar":[
                    { "date": "10-11-2026", "ball":76},
                    { "date": "10-9-2026", "ball":45},
                    { "date": "1-11-2026", "ball":65},
                    { "date": "10-11-2026", "ball":30}
                 ]
            },

                     {
                           "student_name":"lobar",
                           "davomat":[
                               {  "date":"10:11:2026", "status":"kelmadi" } ,
                               {  "date":"10:11:2026", "status":"kelmadi" } ,
                               {  "date":"10:11:2026", "status":"keldi" } ,
                               {  "date":"10:11:2026", "status":"keldi" } ,
                                     ],
           
                           "baholar":[
                               { "date": "10-11-2026", "ball":55},
                               { "date": "10-11-2026", "ball":45},
                               { "date": "10-11-2026", "ball":34},
                               { "date": "10-11-2026", "ball":90}
                                    ]
                       },

                      {
                                "student_name":"mehribon",
                                "davomat":[
                                           {  "date":"10-11-2026", "status":"keldi" } ,
                                           {  "date":"14-9-2026", "status":"kelmadi" } ,
                                           {  "date":"30-10-2026", "status":"keldi" } ,
                                           {  "date":"9:2026", "status":"kelmadi" } ,
                                        ],
                       
                                "baholar":[
                                           { "date": "10-11-2026", "ball":80},
                                           { "date": "10-11-2026", "ball":66},
                                           { "date": "10-11-2026", "ball":54},
                                           { "date": "10-11-2026", "ball":30}
                                        ]
                     }
        ]

    }
]

def find_group(name):
      for group in GROUPS:
            
          if group["name"].lower() == name.lower().strip():
               return group



def add_group():
    group_name = input("Guruh nomini kiriting (add): ").strip()
    if not group_name or len(group_name)<3:
        print("Guruh nomi bo'sh yoki 3 ta harfdan kichik bo'lmasligi kerak")
        return
    group = find_group(group_name)

    if group:
        print("Bunday guruh mavjud")
        return

    GROUPS.append(
        {
            "name": group_name,
            "students": []
        }
    )

    print(f"{group_name} guruhi muvaffaqiyatli qo'shildi")


def show_groups():
     if not GROUPS:
      print("hozircha guruh mavjud emas")
      return
     
     for index, group in enumerate( GROUPS, start=1):
      print(f"{index}. Guruh nomi: {group['name']}  - talabalar soni - {len(group['students'])}")    