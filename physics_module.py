from Question import *
from time import *

def physics_year_2021():
    question_prompts=[
        """1.which of the following quantities is not an example of force
        a. mass
        b. tension
        c. weight
        d. friction
    ""","""2.the reason for laminating the soft iron core of a transformer is to
    a. reduce eddy current
    b. reduce the magnetic flux
    c. increase the magnetic flux
    d. reduce it's efficiency
    ""","""3.Formation of hydrogen bubbles at hte copper plate of a primary cell is called
    a. polarization
    b. back e.m.f
    c. electrolysis
    d. local action
    ""","""4.which of the following factors does not affect the rate of evaporation of a liquid
    a. temperature
    b. volume 
    c. wind 
    d. surface area
    ""","""5.the opening in the eye through which light to the retina is called the 
    a. pupil
    b. cornea
    c. iris
    d. optic nerve
    ""","""6.a heat sensitive resistor made of semi conductor is called a
    a. thermometer 
    b. thermostat
    c. thermistor
    d. thermopile 
    ""","""7.electrical motor primarily converts
    a. electrical energy to chemical energy
    b. kinetic energy to potential energy
    c. electrical energy to mechanical energy
    d. electrical energy to heat energy
    ""","""8.Which of the following statements about molecules of solid and liquids are correct.they both
    a. have weak attraction 
    b. have wide separation
    c. exhibit random motion
    d. exhibit vibratory motion 
    ""","""9.the distance between a node and it's adjacent antinode of a transverse wave is equal to 
    a. half the wave length
    b. the wave length
    c. thrice the wave length
    d. quarter of the wave length
    ""","""10. which of the sketched graph below illustrates the correct variation of the gravitational force,fg,between two objects and the distance,d,between their centres
    a. fg↑
         |
         |  
         |———————————————————    
         |
         |      
         ——————————————————————→
    b.  fg↑
          |      /
          |     /
          |    /
          |   /
          |  /    
          ——————————————————————→   
          
    
    ""","""11.which of the following actions will increase the capacitance of a parallel plate capacitor
             i.   decreasing the distance between the plates
             ii.  increasing the distance between the plates
             iii. increasing the area of the plates overlap
             iv.  avoiding the use of dielelectric between the plates
    a. i and iii only
    b. ii and iii only
    c. i and iv
    d. iii and iv        
    ""","""12.a metallic sphere is heated from 27℃ to 200℃ without change of state.which of the following changes would have resulted from heating?
    a. no changes occur in it's volume and density
    b. it's volume increases and it's density increases
    c. it's volume increases without a change in density
    ""","""13.the acceleration of a moving object cen be determined from the
    a. slope of it's distance time graph
    b. area under it's distance-time graph
    c. slope of it's velocity-time graph
    d. area under it's velocity time graph 
    ""","""14.a student wishes to measure the potential difference across a resistor,R.she has a galvanometer, G and some connecting wires, what else does she need?
    a. high value resistor connected in parallel with G
    b. low value resistor connected in parallel with G 
    c. low value resistor connected in series with G
    d. high value resistor connected in series with G
    ""","""15.the handle of a screwjack is 35cm long and the pitch of the screw is 0.5cm.what force must be applied at the end of the handle to lift a load of 2000N if the efficiency of the jack is 30%?[π=22/7]
    a. 152.0N
    b. 132.0N
    c. 15.2N
    d. 440.0N
    ""","""16.the inductive reactance ina circuit of frequency 100Hz is 1Ω.calculate the inductance of the inductor.[π=3.14]
    a. 2.00 x 10-²
    """
          ]
    questions=[Question(question_prompts[0],"a"),
               Question(question_prompts[1],"a"),
               Question(question_prompts[2],"a"),
               Question(question_prompts[3],"b"),
               Question(question_prompts[4],"a"),
               Question(question_prompts[5],"c"),
               Question(question_prompts[6],"c"),
               Question(question_prompts[7],"d"),
               Question(question_prompts[8],"d"),
               Question(question_prompts[9],"a")
               ]
    def run_test(questions):
        score=0
        for question in questions:
            print("loading please wait")
            sleep(0)
            al=["a","b","c","d","e"]
            answer=input(question.prompt)
            if answer.lower()==question.answer:
                print("you got it right try the next one")
                score+=1
            elif answer.lower()!=al:
                print("sorry you have to input any of the options")
            else:
                print("awwwwm! you are wrong try harder to get the next one.\nthe answer is ,",question.answer)
        print("you got"+str(score)+"/"+str(len(questions))+"correct")
    run_test(questions)
def physics_2017():
    question_prompt = [
        """1. The focal length of a concave  mirror is 2.0 cm. If an object is  placed 8.0cm from it, the image is  at. 
A. 2.7m 
B. 2.3m 
C.2.5m 
D. 2.0m  
""","""2. PHCN measures is electrical  energy in 
A. Wh. 
B. Kwh 
C. J 
D. W. 
""","""3. The resultant of two forces is  50N. If the forces are  perpendicular to each other and  one of them makes an angle 30°  with the resultant. Find its  magnitude.  
A. 100.0N 
B. 57.7N 
C. 25.0N  
D. 43.3N  
""","""4. A piece of radioactive material  contains 1000 atoms. If its half life is 20 seconds, the time taken  for 125 atoms to remain is 
A. 20 seconds 
B. 40 seconds 
C. 60 seconds 
D. 80 seconds
""","""5. In a discharge tube, most of  the gas is pumped out so that  electricity is concluded at 
A. steady voltage 
B. high pressure 
C. low pressure. 
D. low voltage.  
""","""6. I. Moon II. Sun  III. Street light  IV. Stars   Which of the above is a natural  source of light?  
A. I, II and IV only 
B. I, II and III only 
C. III and IV only 
D. II and IV only  
""","""7. An object placed at the bottom  of a well full of clear water  appears closer to the surface due to 
A. refraction. 
B. reflection. 
C. am inverter 
D. a magnifier  
""","""8. A boy drags a bag of rice  along a smooth horizontal flow  with a force of 2N applied at an  angle of 60° to the flow. The work done after a distance of 3m is 
A. 6J. 
B. 4 J 
C. 5 J 
D. 3 J  
""","""9. The spheres of masses 5.0kg  and 10.0kg are 0.3m apart.  Calculate the force of attraction  between them. 
A. 3.57 X 10−2 N. 
B. 3.71 X 10−2 N. 
C. 4.00 X 10−2 N. 
D. 3.50 X 10−2 N. 
""","""10. When very hot water is  poured into two identical thin and  thick glass tumblers in equal  volumes, the thick one cracks  because 
A. of the even expansion of lass. 
B. glass is a good conductor of  heat. 
C. glass is a crystal 
D. of the uneven expansion of  glass   
""","""11. Transverse waves can be  distinguished from longitudinal  waves using the characteristic of  
A. diffraction 
B. reflection. 
C. polarization. 
D. refraction.  
""","""12. Which of the following pairs of  light rays shows the widest  separation in the spectrum of  white light? 
A. Green and yellow. 
B. Blue and red 
C. Indigo and violet 
D. Orange and red.    
""","""13. A transistor functions mainly  as a 
A. switch and an amplifier 
B. rectifier and an amplifier 
C. charge storer and a switch 
D. charge storer and an amplifier 
""","""14. A thin wire with heavy  weights attached to both ends is  hung over a block of ice resting  on two supports. If the wire cuts  through the ice block while the  lock remains solid behind the  wire, the process is called  
A. fusion 
B. sublimation 
C. regelation 
D. condensation. 
""","""15. The inner diameter of a small  test tube can be measured  accurately using a 
A. micrometer screw gauge 
B. pair of Vernier callipers 
C. metre rule 
D. pair of dividers. 
""","""16. A platinum resistance  thermometer records 3.0W at 0°C  and 8/0w at 100°C. If it records  6.0W in a certain environment,  the temperature of the medium is  
A. 60°C 
B. 80°C 
C. 50°C 
D. 30°C 
""","""17. Which of the following is the  dimension of pressure? 16. Which of the following is the  dimension of pressure? 
 A. ML2T−3 
B. MLT−2 
C. ML2−1T−2 
D. ML−3
""","""18. A capacitor 8μF, is charged to  a potential difference of 100V.  The energy stored by the  capacitor is 
 A. 1.0 x 104  
B. 4.0 x 10−2  
C. 1.25 x 10   
D. 8.0 x 10  
""","""19. Which of the following  statements correctly describe(s)  cathode rays?   I. They consist of tiny  particles carrying negative  electric charges  II. They are deflected in a  magnetic field but not in an  electric filed.  III. They consist of fast moving neutrons and  deflected in an electric filed. 
A. I only 
B. III only 
C. I and II only 
D. II and III only.   
""","""20. A concave mirror has a radius  of curvature of 36cm. At what  distance from the mirror should  an object be placed to give a real  image three times the size of the  object? 
A. 12cm 
B. 24cm 
C. 48cm 
D. 108cm 
""","""21. A sonometer wire of length 100cm under a tension of 10N,  has a frequency of 250Hz.  Keeping the length of the wire  constant, the tension is adjusted  to produce a new frequency of  350HZ. The new tension is  
A. 5.1N 
B. 19.6N 
C. 14.0N 
D. 7.1N 
""","""22. In a sound wave in air, the  adjacent rarefactions and  compressions are separated by a  distance of 17cm. If the velocity of the sound wave is 340m −1. Determine the frequency. 
A. 10Hz 
B. 20Hz 
C. 5780Hz 
D. 1000Hz 
""","""23. A note is called an octave of  another note when 
A. the notes have the same  fundamental frequency 
B. its frequency is half of the first note. 
C. its frequency is twice that of  the first note. 
D. its periodic time is twice that of  the first note. 
""","""24. Which of the following is in a  neutral equilibrium? 
A. A heavy weight suspended on a  string 
B. The beam of a balance in use 
C. A heavy-based table lamp 
D. A cone resting on its slant edge 
""","""25. A convex mirror is used as a  driving mirror because   I. Its image is erect  II. It has a large field of view  III. It has a long focal length.  Identify the CORRECT  statement(s). 
A. I and III only 
B. I and II only 
C. II and III only 
D. I, II and III only 
""","""26. What is the cost of running  five 50W lamps and four 100W  lamps for 10 hours if electrical  energy costs 2 kobo per kWh? 
A. ₦ 0.13 
B. ₦ 0.65 
C. ₦ 3.90 
D. ₦39.00 
""","""27. The specific latent heat of  vaporization of a substance is  always 
A. less than its specific latent heat  of fusion 
B. equal to its specific latent heat  of fusion 
C. greater than its specific latent of fusion 
D. all of the above depending on  the nature of the substance.   
""","""28. A hydrometer is an  instrument for measuring the 
A. depth off water in a vessel 
B. relative humidity of the air 
C. relative density of a liquid by  finding the apparent loss in  weight 
D. relative density of a liquid by  the method of flotation  
""","""29. A transformer has 300 turns  of wire in the primary coil and 30  turns in the secondary coil. If the  input voltage is 100 volts, the  output voltage is 
A. 10 volts 
B. 5 volts 
C. 15 volts 
D. 20 volts.   
""","""30. The activity of a radioactive  substance depends on  
A. temperature and purity 
B. purity and age 
C. temperature and age 
D. age, purity and temperature   
""","""31. The speed of light in air is 3 x 108  −1. If the refractive index of light from air-to-water is 4/3, then which of the following is the  correct value of the speed of light  in water? 
 A. 4 x 108m −1 
B. 2.23 x 108m −1 
C. 2.25 x 108m −2 
D. 4/9 x 108m −1  
""","""32. A magnet is moved through a  coil of wire. The e.m.f. produced  in the wire depends on 
A. the number of turns in the coil 
B. the strength of magnet 
C. the speed at which the magnet is moved 
D. all of the above.  
""","""33. A charge of one coulomb  liberated 0.0033g of copper in an  electrolytic process. How long will  it take a current of 2A to liberate  1.98g of copper in such a  process? 
A. 30 minutes 
B. 5 minutes 
C. 50 minutes 
D. 60 minutes. 
    """
    ]
    questions = [Question(question_prompt[0], "A"),
                 Question(question_prompt[1], "B"),
                 Question(question_prompt[2], "D"),
                 Question(question_prompt[3], "D"),
                 Question(question_prompt[4], "C"),
                 Question(question_prompt[5], "D"),
                 Question(question_prompt[6], "A"),
                 Question(question_prompt[7], "C"),
                 Question(question_prompt[8], "B"),
                 Question(question_prompt[9], "D")
                 ]

    def run_test(questions):
        score = 0
        for question in questions:
            print("loading please wait")
            sleep(0)
            answer1 = input(question.prompt)
            if answer1.upper() == question.answer:
                print("you got it right try the next one")
                score += 1
            elif answer1.upper()!=question.answer:
                print("awwwwm! you are wrong try harder to get the next one.\nthe answer is ,", question.answer)
        print("you got" + str(score) + "/" + str(len(questions)) + "correct")
    run_test(questions)
