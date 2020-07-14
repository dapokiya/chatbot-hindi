from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *


bot = ChatBot("my bot")



data = [

    "tell me your  location ?",
    "i am available anytime for you.",

     "Hello",

     "How can you help me ?",
     "Hello ,i am Hindi i help you purchase a INDIAN product ",

     
     "what is your name ?",
     "my name is Hindi ,i am created by dhrupesh ,i help to find out indian product.",

    "Thank you",
    "your Welcome",

    "Bye",
    "Bye,Have a nice day..",

  "Indian Cold Drinks ?" ,
  "Indian Cold Drinks: Kalimark Bovonto, Rose Drink(Sherbat), Badam Drink, Milk, Lassi, Curd, yoghurt, Chaach, Juice, Lemonade(Nimbu Paani), Coconut Water(Naariyal Paani), Shakes, Jaljeera, Thandai, Roohafza (Hamdard), Rasna, Frooti, Godrej Jumpin,",
  "Cold Drinks: Kalimark Bovonto, Rose Drink(Sherbat), Badam Drink, Milk, Lassi, Curd, yoghurt, Chaach, Juice, Lemonade(Nimbu Paani), Coconut Water(Naariyal Paani), Shakes, Jaljeera, Thandai, Roohafza (Hamdard), Rasna, Frooti, Godrej Jumpin,",

    "Indian shop ?",
 "Swadeshi/Indian Soap: Himalaya, Mysoor Sandal, Cinthol, Santoor,Medimix, Neem, Godrej, Patanjali(Kesh Kanti), Wipro, Park Avenue, Swatik, Ayur Herbal, Kesh Nikhar, Hair & Care, Dabur Vatika, Bajaj, Nyle" ,
 "Soap: Himalaya, Mysoor Sandal, Cinthol, Santoor,Medimix, Neem, Godrej, Patanjali(Kesh Kanti), Wipro, Park Avenue, Swatik, Ayur Herbal, Kesh Nikhar, Hair & Care, Dabur Vatika, Bajaj, Nyle",

    "Indian Toothpaste ?",
"Swadeshi/Indian Toothpaste: Neem, babool, vicco, dabur, Vico Bajradanti, MDH, Baidyanath, Gurukul Pharmacy, Choice, Anchor, Meswak, Babool, Promise, Patanjali(Dant Kanti, Dant Manjan).",
"Toothpaste: Neem, babool, vicco, dabur, Vico Bajradanti, MDH, Baidyanath, Gurukul Pharmacy, Choice, Anchor, Meswak, Babool, Promise, Patanjali(Dant Kanti, Dant Manjan).",



"Indian Toothbrush ?",
"Swadeshi/Indian Toothbrush: Ajay, Promise, Ajanta, Royal, Classic, Dr. Strock, Monate.",
"Toothbrush: Ajay, Promise, Ajanta, Royal, Classic, Dr. Strock, Monate.",


"Indian Tea & Coffee ?",
"Swadeshi/Indian Tea & Coffee: Divya Peya(Patanjali), Tata, Brahmaputra, Aasam, Girnaar, Indian Cafe, M.R.,AVT Tea,  Narasus Coffee, Leo Coffee ",
"Tea & Coffee: Divya Peya(Patanjali), Tata, Brahmaputra, Aasam, Girnaar, Indian Cafe, M.R.,AVT Tea,  Narasus Coffee, Leo Coffee ",


"Indian Blade ?",
"Swadeshi/Indian Blade: Topaz, Gallant, Supermax, Laser, Esquire, Silver Prince, Premium.",
"Blade: Topaz, Gallant, Supermax, Laser, Esquire, Silver Prince, Premium.",



"Indian Shaving Cream ?",
"Swadeshi/Indian Shaving Cream: Park Avenue, Premium, Emami, Balsara, Godrej, Nivea.",
"Shaving Cream: Park Avenue, Premium, Emami, Balsara, Godrej, Nivea.",

"Indian Shampoo ?",
"Swadeshi/Indian Shampoo: Himalaya, Nirma, Velvette",
"Shampoo: Himalaya, Nirma, Velvette",


"Indian Talcum Powder ?",
"Swadeshi/Indian Talcum Powder: Santoor, Gokul,Cinthol, Boroplus, Cavin Kare Products",
"Talcum Powder: Santoor, Gokul,Cinthol, Boroplus, Cavin Kare Products",


"Indian Milk ?",
"Swadeshi/Indian Milk: Amul, Amulya, Mother Dairy",
"Milk: Amul, Amulya, Mother Dairy",


"Indian Mobile Connection ?",
"Swadeshi/Indian Mobile Connection: Idea, Airtel, Reliance, Bsnl",
"Mobile Connection: Idea, Airtel, Reliance, Bsnl",



"Indian Textiles or Clothes ?",
"Swadeshi/Indian Textiles or Clothes: Raymond, SiyaRam, Bombay Dyeing, S. Kumars, Mafatlal, Garden Vareli, American Swan, Gini & Jony, Globus, Madame, Monte Carlo Fashions Limited, Reliance Retail, RmKV",
"Textiles or Clothes: Raymond, SiyaRam, Bombay Dyeing, S. Kumars, Mafatlal, Garden Vareli, American Swan, Gini & Jony, Globus, Madame, Monte Carlo Fashions Limited, Reliance Retail, RmKV",


"Indian Mobile ?",
"Swadeshi/Indian Mobile: Micromax,  Karbonn, Lava",
"Mobile: Micromax,  Karbonn, Lava",


"Indian Bikes ?",
"Swadeshi/Indian Bikes: Hero, Bajaj, TVS BIKES AND AUTO RICKSHAWS",
"Bikes: Hero, Bajaj, TVS BIKES AND AUTO RICKSHAWS",

"Indian Footwear ?",
"Swadeshi/Indian Footwear: Paragon, Lakhani , Chavda, Khadims, VKC Pride, Lunar Footwear",
"Footwear: Paragon, Lakhani , Chavda, Khadims, VKC Pride, Lunar Footwear",


"Indian Jeans ?",
"Swadeshi/Indian Jeans and T-shirts: Spykar, K-lounge",
"Swadeshi/Indian Jeans and T-shirts: Spykar, K-lounge",

"Indian T-shirts ?",
"Swadeshi/Indian Jeans and T-shirts: Spykar, K-lounge",
"Swadeshi/Indian Jeans and T-shirts: Spykar, K-lounge",

"Indian GARMENTS ?",
"Swadeshi/Indian GARMENTS: Cambridge, Park Avenue, Bombay Dyeing, Ruf & Tuf, Trigger Jeans, Lakhani, Shreelathers, Khadim, khadi, Action",
"GARMENTS: Cambridge, Park Avenue, Bombay Dyeing, Ruf & Tuf, Trigger Jeans, Lakhani, Shreelathers, Khadim, khadi, Action",


"Indian Watches ?",
"Swadeshi/Indian Watches: Titan, HMT, Maxima, Prestige, Ajanta, Fasttrack.",
"Watches: Titan, HMT, Maxima, Prestige, Ajanta, Fasttrack.",


"Indian Child Food ?",
"Swadeshi/Indian Child Food: Honey, Boiled rice, Fruit Juice. Amul, Sagar, Tapan, Milk Care, etc.",
"Child Food: Honey, Boiled rice, Fruit Juice. Amul, Sagar, Tapan, Milk Care, etc.",


"Indian Salt ?",
"Swadeshi/Indian Salt: Tata, Ankur, Saindha namak(Patanjali), Low Sodium & Iron-45 Ankur, Tata, Surya, Tara.",
"Salt: Tata, Ankur, Saindha namak(Patanjali), Low Sodium & Iron-45 Ankur, Tata, Surya, Tara.",


"Indian Icecream ?",
"Swadeshi/Indian Icecream: Homemade icecream/coolfi, Amul, Vadilal, Arun Ice Cream, Milk food, etc.",
"Icecream: Homemade icecream/coolfi, Amul, Vadilal, Arun Ice Cream, Milk food, etc.",


"Indian Biscuits ?",
"Swadeshi/Indian Biscuits: Parle, Sunfeast, Britannia, Tiger, Indana, Amul, Ravalgaon, Bakemens, Creamica, Shagrila, Patanjali(Amla Candy, Bel Candy, Aarogya biscuit).",
"Biscuits: Parle, Sunfeast, Britannia, Tiger, Indana, Amul, Ravalgaon, Bakemens, Creamica, Shagrila, Patanjali(Amla Candy, Bel Candy, Aarogya biscuit).",


"Indian Ketchup ?",
"Swadeshi/Indian Ketchup and Jam: Homemade sauce/ketchup, Indana, Priya, Rasna, Patanjali(Fruit jam, Apple jam, Mix jam).",
"Ketchup and Jam: Homemade sauce/ketchup, Indana, Priya, Rasna, Patanjali(Fruit jam, Apple jam, Mix jam).",

"Indian Jam ?",
"Swadeshi/Indian Ketchup and Jam: Homemade sauce/ketchup, Indana, Priya, Rasna, Patanjali(Fruit jam, Apple jam, Mix jam).",
"Ketchup and Jam: Homemade sauce/ketchup, Indana, Priya, Rasna, Patanjali(Fruit jam, Apple jam, Mix jam).",

"Indian Snakc ?",
"Swadeshi/Indian Snacks:Balaji, Bikano Namkeen, Haldiram, Homemade chips, Bikaji, AOne,Gopal, etc.",
"Snacks:Balaji, Bikano Namkeen, Haldiram, Homemade chips, Bikaji, AOne,Gopal, etc.",


"Indian Water ?",
"Swadeshi/Indian Water: Home-boiled pure water, Ganga, Himalaya, Rail neer, Bisleri.",
"Water: Home-boiled pure water, Ganga, Himalaya, Rail neer, Bisleri.",


"Indian Tonic ?",
"Swadeshi/Indian Tonic: Patanjali(Badam Pak, Chyawanprash, Amrit Rasayan, Nutramul)",
"Tonic: Patanjali(Badam Pak, Chyawanprash, Amrit Rasayan, Nutramul)",


"Indian Oil ?",
"Swadeshi/Indian Oil: Param Ghee, Amul, Handmade cow ghee, Patanjali(Sarso ka tel)",
"Oil: Param Ghee, Amul, Handmade cow ghee, Patanjali(Sarso ka tel)",


"Indian Washing ?",
"Swadeshi/Indian Washing: Tata Shudh, Nima, Care, Sahara, Swastik, Vimal, Hipolin, Fena, Sasa, TSeries, Dr. Det, Ghadi, Genteel, Ujala, Ranipal, Nirma, Chamko, Dip",
"Washing: Tata Shudh, Nima, Care, Sahara, Swastik, Vimal, Hipolin, Fena, Sasa, TSeries, Dr. Det, Ghadi, Genteel, Ujala, Ranipal, Nirma, Chamko, Dip",


"Indian Cosmetics ?",
"Swadeshi/Indian Cosmetics: Neem, Borosil, Ayur Emami, Vico, Boroplus, Boroline, Himani Gold, Nyle, Lavender, Hair & Care, Heavens, Cinthol, Glory, Velvet(Baby).",
"Cosmetics: Neem, Borosil, Ayur Emami, Vico, Boroplus, Boroline, Himani Gold, Nyle, Lavender, Hair & Care, Heavens, Cinthol, Glory, Velvet(Baby).",


"Indian pen ?",
"Swadeshi/Indian Pen: Camel, Kingson, Sharp, Cello, Natraj, Ambassador, Linc, Montex, Steek, Sangita, Luxor.",
"Pen: Camel, Kingson, Sharp, Cello, Natraj, Ambassador, Linc, Montex, Steek, Sangita, Luxor.",


"Indian Electronics ?",
"Swadeshi/Indian Electronics: Voltas, Videocon, BPL, Onida, IFB, Orpat, Oscar, Salora, ET&T, T-series, Nelco, Weston, Uptron, Keltron, Cosmic, TVS, Godrej, Brown, Bajaj, Usha, Polar, Anchor, Surya, Oriont, Cinni, Tullu, Crompton, Loyds, Blue Star, Voltas, Cool home, Khaitan, Everready, Gee",
"Electronics: Voltas, Videocon, BPL, Onida, IFB, Orpat, Oscar, Salora, ET&T, T-series, Nelco, Weston, Uptron, Keltron, Cosmic, TVS, Godrej, Brown, Bajaj, Usha, Polar, Anchor, Surya, Oriont, Cinni, Tullu, Crompton, Loyds, Blue Star, Voltas, Cool home, Khaitan, Everready, Gee",


"Indian Computer ?",
"Swadeshi/Indian Computer & Tablets: HCL, MICROMAX, SPICE, Reliance, Carbonn, Amar PC, Chirag",
"Computer & Tablets: HCL, MICROMAX, SPICE, Reliance, Carbonn, Amar PC, Chirag",

"Indian Tablets ?",
"Swadeshi/Indian Computer & Tablets: HCL, MICROMAX, SPICE, Reliance, Carbonn, Amar PC, Chirag",
"Computer & Tablets: HCL, MICROMAX, SPICE, Reliance, Carbonn, Amar PC, Chirag",

"Indian Online Shopping site ?",
"Swadeshi/Indian Online Shopping Site : Flipkart, IndiaPlaza, YeBhi, Myntra,Naaptol, SnapDeal, HomeShop18, bookmyShow, makemytrip, yatra, via, ibibo, cleartrip.",
"Online Shopping Site : Flipkart, IndiaPlaza, YeBhi, Myntra,Naaptol, SnapDeal, HomeShop18, bookmyShow, makemytrip, yatra, via, ibibo, cleartrip.",


"Indian Car Company ?",
"Swadeshi/Indian Car: TATA, Mahindra, Hindustan Motors, Maruti",
"Car: TATA, Mahindra, Hindustan Motors, Maruti"


]
trainer = ListTrainer(bot)

trainer.train(data)





main = Tk()
main.geometry("500x650")
main.title("Hindi")

img =PhotoImage(file="hindi.png")
photol=Label(main, image=img)
photol.pack(pady=5)

def hindians():
    userinput = text.get()
    ans = bot.get_response(userinput)
    msg.insert(END, "YOU :" + userinput)
    msg.insert(END, "Hindi :" + str(ans))
    text.delete(0, END)

frame = Frame(main)
sc = Scrollbar(frame)
#sc1 = Scrollbar(frame)
msg = Listbox(frame, width=80, height=20)
sc.pack(side=RIGHT, fill=Y)
#sc1.pack(side=BOTTOM, fill=X)
msg.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()


text = Entry(main, font=("Verdana", 20), bd=4)
text.pack(fill=X, pady=10, side=LEFT)

btn = Button(main, text="send", font=("Verdana", 20), command=hindians)
btn.pack(fill=X, pady=10, side=RIGHT)







main.mainloop()