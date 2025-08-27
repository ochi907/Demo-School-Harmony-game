# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Define the bounce transform

  



# Define charactersjh
define p = Character("[player_name]", color="#060806")
define teacher = Character("ครูนา", color="#ffc8c8") # มีภาพ
define bam = Character("แบมแบม", color="#ffc0ff") # มีภาพ
define meen = Character("มีน", color="#c8c8ff") # มีภาพ
define meen_mom = Character("แม่มีน",color="#ff2d2d80")
define kao = Character("เก้า", color="#ffffc8") # มีภาพ
define boss = Character("บอส", color="#ff4444") # มีภาพ
define angie = Character("แองจี้", color="#ff77aa") # มีภาพ
define narrator = Character(None)


# Initialize trust variables
default trust_meen = 0
default trust_bam = 0

label start:
    scene frontschool with fade
    play music "background music.mp3" 
    narrator "วันเปิดเทอมใหม่... กลิ่นแดดบนสนามกับเสียงจ๊อกแจ๊กจอแจของนักเรียน"
    narrator "คุณเดินเข้าสู่โรงเรียนใหม่ด้วยหัวใจเต้นแรง กระเป๋านักเรียนสะพายอยู่ข้างหลัง เสื้อผ้ากระดุมเรียบร้อย"
    narrator "แต่สายตายังสอดส่องไปรอบ ๆ โรงเรียนที่กว้างใหญ่และไม่คุ้นเคย"
    scene before_class with fade
    stop music fadeout 1.0
    play music "hallway.mp3" fadein 1.0
    narrator "เช้าวันแรกของเทอมใหม่ แสงแดดอ่อน ๆ สาดส่องผ่านหน้าต่างโรงเรียน ทำให้บรรยากาศอบอุ่นและเต็มไปด้วยความหวัง"
    scene classroom-background with dissolve
    stop music fadeout 1.0
    play music "bell.mp3" noloop
    narrator "เสียงกระดิ่งดังขึ้น เหล่านักเรียนทยอยเข้าห้อง คุณมองเพื่อน ๆ รอบตัว มีทั้งคนที่หัวเราะคุยกันอย่างสนุกสนาน"
    narrator "และคนที่ยืนเงียบเหมือนคุณเอง รอยยิ้มที่ไม่กล้าสบตาทำให้คุณรู้สึกทั้งตื่นเต้นและประหม่าพร้อมกัน"
    narrator "เด็กนักเรียนทยอยเข้าห้องด้วยชุดนักเรียนเรียบร้อย เสียงหัวเราะ เสียงทักทายกันเบา ๆ คลอไปกับกลิ่นดินเหนียวอ่อน ๆ จากสวนด้านนอก"
    scene in_class with dissolve
    narrator "คุณเดินไปหาที่นั่งว่างและพยายามทำใจให้สงบ"
    show kruna talk
    teacher "เอาล่ะนักเรียนทุกคน ถึงเวลาเข้าคาบเรียนของเราแล้ว"
    teacher "ครูชื่อนานะคะ เป็นที่ปรึกษาของพวกเราในปีนี้"
    show kruna happy
    teacher "ยินดีต้อนรับนักเรียนทุกคนสู่ปีการศึกษาใหม่นะคะ งั้นเดี๋ยวเรามาทำความรู้จักกันก่อนดีกว่า"
    show kruna talk
    teacher "อืม...เริ่มจากเธอก่อนเลยแล้วกัน"
    narrator "ครูนาพูดแล้วหันมาทางคุณ"

    hide kruna
    $ player_name = renpy.input("กรอกชื่อของคุณ:", length=20)
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name = "คุณนักเรียนใหม่"
    menu:
        "คุณจะแนะนำตัวแบบไหน?"
        "แนะนำตัวแบบมั่นใจ":
            $ intro_style = "confident"
            p "สวัสดี! เราชื่อ[player_name] ฝากเนื้อฝากตัวด้วยนะ!"
        "แนะนำตัวแบบขี้อาย":
            $ intro_style = "shy"
            p "อะ...เอ่อ...เราชื่อ[player_name]  ยินดีที่ได้รู้จักนะทุกคน..."
        "แนะนำตัวแบบกวนๆ":
            $ intro_style = "funny"
            p "เรา[player_name]  ยินดีที่ได้รู้จักนะเว้ยพวก ฮ่าๆ!"


    scene black 
    window hide
    show text "หลังจากนั้นทุกคนก็ออกมาแนะนำตัวจนครบ" at truecenter
    
    pause 2.0
    window show
    scene in_class with dissolve
    show kruna talk
    teacher "ต่อไปจะเป็นกิจกรรมจับกลุ่มกัน เพื่อเล่น Ice-breaking กันนะ คงรู้จักกิจกรรมนี้กันอยู่แล้วเนอะ"
    hide kruna tslk
    
    show bambam talk 
    bam "รู้จักค่า!"
    hide bambam talk

    show kruna talk 
    teacher "ดีเลย งั้นครูปล่อยให้จับกลุ่มเลยแล้วกันนะ"
    hide kruna talk

    show gao talk with fade
    kao "เฮ้[player_name]! มานี่เลย กลุ่มเราขาดคนพอดี!"
    hide gao talk
    show gao normal
    narrator "คุณเดินไปทางกลุ่มของเก้า"
    hide gao
    show gao talk 
    kao "คุยด้วยได้นะเพื่อน ไม่ต้องเกร็ง สนิทกันไว้ ฮ่าๆ!" 
    hide gao talk
    show gao normal
    p "อื้ม! ว่าแต่พวกเธอชื่ออะไรกันบ้างหรอ"
    show gao talk
    kao "เราชื่อเก้า ส่วนข้างๆ เราชื่อแบม"
    hide gao talk
    show gao normal
    show  bambam talk at right
    bam "หวัดดีเราแบม แกชื่อ[player_name]ใช่ปะ ยินดีที่ได้รู้จักนะ"
    hide bambam talk
    show bambam normal at right
    p "ยินดีที่ได้รู้จักเหมือนกันนะแบม"
    p "แบมดูดีจังเลยอ่ะ สวยสะดุดตาสุดๆ"
    hide bambam normal 
    show  bambam happy at right
    bam "จริงหรอ แกนี่ปากหวานนะเนี่ย ชมกันแบบนี้ก็เขินแย่เลยสิ"
    hide bambam happy
    show bambam normal at right
    show gao talk
    kao "เขาหลอกก็เชื่อเนอะเธอนี่"
    hide gao talk
    show gao normal
    show bambam angry at right
    bam "อะไรยะ [player_name]พูดจริงต่างหาก ใช่ปะ!"
    show gao happy
    kao "อย่าไปชมแบมมากนะ[player_name] ยัยนี่น่ะบ้ายอสุดๆ"
    hide bambam angry
    show bambam talk at right
    bam "อิจฉาหรอที่ฉันมีคนชม ขัดฟีลกันตลอดเลยอะ"
    hide bambam talk
    show bambam normal at right
    show gao angry
    kao "ใครจะอิจฉาคนอย่างเธอไม่ทราบ"
    hide gao angry
    show gao normal
    p "ฮ่าๆ เพิ่งจะวันแรกทำไมสองคนถึงดูสนิทกันจังเลย"
    hide bambam normal
    show bambam talk at right
    bam "อ่อ! พอดีเรากับเก้าเป็นเพื่อนกันมาตั้งแต่สมัยมัธยมต้นแล้วน่ะ"
    hide bambam talk
    hide gao normal
    p "แบบนี้นี่เอง ดีจังเลยนะ"
    show bambam talk 
    bam "แต่ว่าน้า อยู่แค่สองคนนี่เหงาจะตายไป"
    hide bambam talk
    show bambam happy
    bam "ถ้ามี[player_name]มาอยู่ด้วย ชีวิตมัธยมปลายต้องสนุกมากแน่ๆ!"
    hide bambam happy
    show bambam normal 
    p "จริงหรอ งั้นจากนนี้ฉันขออยู่กับพวกเธอนะ"
    hide bambam normal
    show bambam happy 
    bam "อื้ม! ได้สิ"
    hide bambam happy
    narrator "คุณกับแบมคุยเล่นด้วยกันไปซักพักแล้วเก้าพูดขึ้นมา"
    
    show gao normal with fade
    kao "อืม... ทีนี้ก็ขาดอีกหนึ่งคนสินะ"
    narrator "คุณมองไปรอบ ๆ ห้องเพื่อสังเกตว่าใครยังไม่มีกลุ่ม"
    hide gao normal
    p "นี่ๆ ผู้หญิงคนนั้นไง นั่งอยู่ตรงนั้นคนเดียวคงยังไม่มีกลุ่มแน่ ๆ"
    show bambam worry 
    bam "โอ๊ย ไม่เอาๆๆ อย่าเอามีนมาอยู่นะ ยัยนั่นเงียบจะตาย มาอยู่กลุ่มเดียวกันคงง่วงกันทั้งหมดพอดี"
    narrator "คุณตกใจกับสิ่งที่แบมพูด" 
    p "เดี๋ยวสิแบม... ทำไมไปพูดกับเพื่อนแบบนั้น"
    hide bambam worry
    show bambam happy
    bam "ฮ่าๆ ล้อเล่นน่า! มีนมานี่เร็ว"
    hide bambam happy 


    show meen sad with fade
    meen "แบมชอบแกล้งกันทุกทีเลย เราจะคิดว่าแบมไม่ชอบเราจริงๆ แล้วนะ"
    show  bambam talk at right
    bam "ไม่ใช่นะ ที่แกล้งก็เพราะตอนมีนทำหน้าตกใจมันดูน่ารักดีนี่นา"
    hide meen sad
    show meen angry 
    meen "..."
    hide bambam talk
    show  bambam happy at right
    bam "ทำเป็นงอนนะเดี๋ยวนี้ แกล้งนิดหน่อยเอง ไม่งอนกันน้า"
    hide meen sad
    hide bambam happy

    narrator "บอสกับแองจี้เดินเข้ามาทางกลุ่มที่คุณอยู่"
    show boss normal at left
    boss "เหอะ...เห็นไหม? เงียบจนใครเขาก็ไม่อยากเอาเข้ากลุ่ม"
    show angie normal at right
    angie "ใช่! อย่าไปเสียเวลาร่วมกลุ่มกับคนแบบนั้นเลย"
    menu:
        "คุณจะตอบยังไง?"
        "ปกป้องมีน":
            p "ทำไมพูดแบบนี้กับเพื่อนล่ะ? มีนอาจจะดีกว่าพวกเธอคิดก็ได้นะ"
            show  angie happy
            angie "มีดีอะไรล่ะ ดีแต่นั่งใบ้สิไม่ว่า ฮ่าๆๆๆ!"
            p "อืม... เราว่าก็ดีกว่าพูดมากแต่พูดจาไร้แก่นสารแบบนี้นะ"
            hide angie normal
            show angie angry at right
            angie "นี่แก..."
            hide angie angry 
            hide boss normal
            show kruna angry with moveinright
            teacher "เฮ้ นี่ครูให้พวกเธอทำกิจกรรมละลายพฤติกรรมเพื่อกระชับมิตรกันนะ"
            teacher "ทำไมถึงจะมาทะเลาะกันได้เนี่ย"
            teacher "พวกเธอหยุดการกระทำแบบนี้เลยนะ"
            hide kruna angry
            show boss angry
            boss "เหอะ อย่าทำเป็นได้ใจมากไปหน่อยเลย"
            show angie angry
            angie "ชิ! ฝากไว้ก่อนเถอะ"
            scene black 
            window hide
            show text "คุณและเพื่อนๆ ไม่สนใจและเข้าร่วมกิจกรรมด้วยกันจนถึงเวลาพักกลางวัน" at truecenter
            pause 2.0
            window show

        "ไม่พูดอะไร":
            p "..."
            hide boss normal
            show bambam talk at left
            bam "นี่พวกเธอเป็นอะไรกัน ฉันแค่หยอกเล่นกับเพื่อนฉัน พวกเธอมายุ่งอะไรด้วยเนี่ย"
            show  angie happy at right
            angie "อุ๊ยแบม พูดจาให้มันดีๆ หน่อยสิ นี่ก็เข้ามาคุยเล่นด้วยเฉยๆ เองนะ"
            show bambam happy at left
            bam "แล้วฉันพูดจาไม่ดีตรงไหนหรอ แค่ถามเองนะ ว่าพวกเธอมา..ยุ่ง! อะไรด้วย"
            show  angie angry at right
            angie "นี่แกว่าฉันหรอ!"
            angie "ฉ..ฉันจะฟ้องครูนา!"
            show bambam talk at left
            bam "เอาซิ แต่จะฟ้องอะไรล่ะ เธอเป็นฝ่ายเข้ามาหาเรื่องพวกฉันก่อนนะ"
            show  angie talk at right
            angie "ฮึ...เดี๋ยวเธอก็รู้"
            hide bambam talk
            hide angie talk
            narrator "แองจี้ยิ้มใส่่จากนั้นเธอก็เริ่มก้มหน้าลงไปแล้วบีบน้ำตา"
            show  angie sad
            show bambam angry at right
            bam "นี่พยายามจะอะไรของเธอ"
            hide bambam angry 
            show boss talk at left
            boss "คุณครูครับ!! เพื่อนทะเลาะกันครับ!!"
            hide boss talk
            show kruna angry with moveinright 
            teacher "นี่มันเกิดอะไรขึ้น!"
            hide kruna angry
            show angie sad
            angie "ฮึก... คุณครูคะ...แบมเขาน่ะค่ะ อยู่ดี ๆ ก็มาด่าหนู"
            angie "ทั้งที่หนูแค่จะเข้ามาคุยเล่นกับมีนเองนะคะ.."
            show bambam angry at right
            bam "นี่! พูดอะไรก็ให้มันจริงหน่อยเถอะ คุยเล่นบ้าบออะไรของเธอ เธอเข้ามาพูดหาเรื่องเราต่างหาก"
            hide bambam angry
            show bambam sad at right
            bam "ไม่จริงนะคะคุณครู แองจี้กับบอสเดินมาแล้วก็พูดจาไม่ดีใส่มีนค่ะ หนูแค่ปกป้องเพื่อนของหนู"
            hide bambam sad
            hide angie sad
            show kruna angry
            narrator "คุณครูนามองหน้าแองจี้และแบมก่อนที่จะหันมาถามคุณ"
            hide kruna angry
            show kruna talk 
            teacher "หนูช่วยเล่าให้ครูฟังหน่อยได้ไหม ว่าเหตุการณ์เป็นมายังไง ตั้งแต่เริ่มต้น"
            hide kruna talk
            show kruna normal
            narrator "คุณเล่าเหตุการณ์ทั้งหมดตั้งแต่เริ่มต้นให้ครูนาฟัง"
            hide kruna normal
            show kruna talk
            teacher "เรื่องทั้งหมดเป็นแบบนี้นี่เอง ครูเข้าใจแล้วล่ะ"
            hide kruna talk
            show kruna angry
            teacher "แองจี้ เธอรู้ใช่ไหมว่าการกระทำของเธอมันควรหรือไม่ควร"
            hide kruna angry
            show kruna normal
            show angie sad at right
            angie "..."
            hide kruna normal
            show kruna angry
            teacher "จบคาบนี้เธอไปพบครูที่ห้องพักครูด้วย"
            angie "ค่ะคุณครู..."
            hide kruna angry
            hide angie sad
            narrator "แองจี้หันมามองทางกลุ่มคุณ"
            show angie angry
            angie "ฝากไว้ก่อนเถอะพวกแก"
            hide angie angry
            scene black 
            window hide
            show text "คุณและเพื่อนๆ ไม่สนใจและเข้าร่วมกิจกรรมด้วยกันจนถึงเวลาพักกลางวัน" at truecenter
            pause 2.0
            window show


        "เข้าข้างบอสกับแองจี้":
            p "ก็จริงของบอสกับแองจี้นะ บรรยากาศรอบตัวมีนดูน่าเบื่อจะตาย"
            angie "ใช่มั้ยล่ะ! ดีแล้วล่ะที่แกคิดแบบนั้น"
            narrator "คุณหันไปเจอแบมกับเก้าที่ทำหน้าเหมือนจะผิดหวังในตัวคุณเล็กน้อย"
            show bambam talk at left
            bam "นี่พวกเธอเป็นอะไรกัน ฉันแค่หยอกเล่นกับเพื่อนฉัน พวกเธอมายุ่งอะไรด้วยเนี่ย"
            show  angie happy at right
            angie "อุ๊ยแบม พูดจาให้มันดีๆ หน่อยสิ นี่ก็เข้ามาคุยเล่นด้วยเฉยๆ เองนะ"
            show bambam happy at left
            bam "แล้วฉันพูดจาไม่ดีตรงไหนหรอ แค่ถามเองนะ ว่าพวกเธอมา..ยุ่ง! อะไรด้วย"
            show  angie angry at right
            angie "นี่แกว่าฉันหรอ!"
            angie "ฉ..ฉันจะฟ้องครูนา!"
            show bambam talk at left
            bam "เอาซิ แต่จะฟ้องอะไรล่ะ เธอเป็นฝ่ายเข้ามาหาเรื่องพวกฉันก่อนนะ"
            show  angie talk at right
            angie "ฮึ...เดี๋ยวเธอก็รู้"
            hide bambam talk
            hide angie talk
            narrator "แองจี้ยิ้มใส่่จากนั้นเธอก็เริ่มก้มหน้าลงไปแล้วบีบน้ำตา"
            show  angie sad
            show bambam angry at right
            bam "นี่พยายามจะอะไรของเธอ"
            hide bambam angry 
            show boss talk at left
            boss "คุณครูครับ!! เพื่อนทะเลาะกันครับ!!"
            hide boss talk
            show kruna angry with moveinright 
            teacher "นี่มันเกิดอะไรขึ้น!"
            hide kruna angry
            show angie sad
            angie "ฮึก... คุณครูคะ...แบมเขาน่ะค่ะ อยู่ดี ๆ ก็มาด่าหนู"
            angie "ทั้งที่หนูแค่จะเข้ามาคุยเล่นกับมีนเองนะคะ.."
            show bambam angry at right
            bam "นี่! พูดอะไรก็ให้มันจริงหน่อยเถอะ คุยเล่นบ้าบออะไรของเธอ เธอเข้ามาพูดหาเรื่องเราต่างหาก"
            hide bambam angry
            show bambam sad at right
            bam "ไม่จริงนะคะคุณครู แองจี้กับบอสเดินมาแล้วก็พูดจาไม่ดีใส่มีนค่ะ หนูแค่ปกป้องเพื่อนของหนู"
            hide bambam sad
            hide angie sad
            show kruna angry
            narrator "คุณครูนามองหน้าแองจี้และแบมก่อนที่จะหันมาถามคุณ"
            hide kruna angry
            show kruna talk 
            teacher "หนูช่วยเล่าให้ครูฟังหน่อยได้ไหม ว่าเหตุการณ์เป็นมายังไง ตั้งแต่เริ่มต้น"
            hide kruna talk
            show kruna normal
            narrator "คุณเล่าเหตุการณ์ทั้งหมดตั้งแต่เริ่มต้นให้ครูนาฟัง"
            hide kruna normal
            show kruna talk
            teacher "เรื่องทั้งหมดเป็นแบบนี้นี่เอง ครูเข้าใจแล้วล่ะ"
            hide kruna talk
            show kruna angry
            teacher "แองจี้ เธอรู้ใช่ไหมว่าการกระทำของเธอมันควรหรือไม่ควร"
            hide kruna angry
            show kruna normal
            show angie sad at right
            angie "..."
            hide kruna normal
            show kruna angry
            teacher "จบคาบนี้เธอไปพบครูที่ห้องพักครูด้วย"
            angie "ค่ะคุณครู..."
            hide kruna angry
            hide angie sad
            narrator "แองจี้หันมามองทางกลุ่มคุณ"
            show angie angry
            angie "ฝากไว้ก่อนเถอะพวกแก"
            hide angie angry
            scene black 
            window hide
            show text "คุณและเพื่อนๆ ไม่สนใจและเข้าร่วมกิจกรรมด้วยกันจนถึงเวลาพักกลางวัน" at truecenter
            pause 2.0
            window show



    scene cafeteria with fade
    narrator "พักเที่ยงมาถึง คุณมองหาโต๊ะว่าง ๆ เพื่อไปนั่งกินข้าว"
    menu:
        "คุณจะนั่งกับใคร?"
        "นั่งกับมีน":
            $ trust_meen += 1 
            p "มีน! ทำไมมานั่งคนเดียวล่ะเนี่ย"
            show meen sad
            meen "คือ...เมื่อกี้นี้คนเยอะมากๆ ทำให้เราหลงกับแบม"
            meen "เราไม่รู้จะไปไหน เลยมานั่งตรงนี้คนเดียว..."
            p "ฮ่าๆ เธอนี่นะ"
            p "มาๆ เดี๋ยวเรานั่งเป็นเพื่อน"
            narrator "คุณหันไปยิ้มให้มีนหลังพูดจบ ก่อนที่จะนั่งลงที่เก้าอี้ฝั่งตรงข้ามมีน"
            hide meen sad
            show meen happy
            meen "..."
            hide meen happy
            show meen sad
            meen "เอ่อ...[player_name]"
            p "หือ ว่าไงมีน"
            hide meen sad
            show meen talk
            meen "ขอบคุณนะ...ที่มานั่งกับเรา"
            hide meen talk
            show meen sad
            meen "ที่ผ่านมา เพราะเราพูดไม่ค่อยเก่ง ไม่ค่อยกล้า...เข้าหาคนอื่น"
            meen "ตลอดช่วงมัธยมต้นเลยทำให้เราไม่มีเพื่อน...แถมยังโดนเพื่อนแกล้งอยู่บ่อยๆ..."
            hide meen sad
            show meen normal
            p "ถ้าให้เดาพวกที่แกล้งเธอคงเป็นแองจี้กับบอสสินะ"
            hide meen normal
            show meen sad
            meen "..."
            p "แล้วแบมกับเก้าล่ะ"
            hide meen sad
            show meen talk
            meen "ตอนมัธยมต้นเราอยู่คนละห้องกับแบมแล้วก็เก้าน่ะ.."
            hide meen talk
            show meen normal
            p "เธอคงอดทนมาตลอดเลยสินะ"
            p "เก่งมากๆ เลยนะมีน จากนี้เราจะเป็นเพื่อนกับเธอเอง แบมกับเก้าก็ด้วย"
            hide meen normal
            show meen sad
            meen "ขอบคุณนะ[player_name]... ขอบคุณมากจริงๆ"
            p "อย่าร้องสิ มาๆ กินข้าวกันเถอะ"
            hide meen sad
            show meen happy
            meen "อื้อ"
            hide meen happy
            scene black 
            window hide
            show text "คุณกับมีนทานข้าวด้วยกันจนเสร็จเรียบร้อย" at truecenter
            pause 2.0
            window show
            scene walkway with fade
            show meen talk
            meen "เดี๋ยวเราไปเข้าห้องน้ำนะ"
            hide meen talk
            show meen normal
            p "โอเค ให้เราไปเป็นเพื่อนไหม"
            hide meen normal
            show meen talk
            meen "ไม่เป็นไรๆ [player_name]ไปรอที่ห้องเถอะ"
            hide meen talk
            show meen happy
            p "ตามใจเธอแล้วกัน"


            
    
        "นั่งกับเก้า":
            show gao talk at right
            kao "มาเร็ว[player_name] ที่นี่ว่างพอดี!"
            hide gao talk
            narrator "คุณเดินไปนั่งกับเก้าและแบม"
            show gao normal
            p "มีนล่ะ?"
            show bambam talk
            bam "นั่นสิ...เมื่อกี้ยังเดินมาด้วยกันอยู่เลย"
            hide bambam talk
            show bambam normal
            show gao talk
            kao "คงจะหลงกันตอนเดินหาที่นั่งแหละมั้ง"
            kao "หรือไม่ก็อาจจะชอบกินอะไรคนเดียวก็ได้"
            hide gao talk
            show gao normal
            show bambam talk
            bam "ถ้าเพราะอย่างนั้นจริงๆ ก็ค่อยหายห่วงนิดนึงแหละนะ"

        "นั่งคนเดียว":
            narrator "คุณเลือกที่จะนั่งคนเดียว และสังเกตบรรยากาศรอบตัว"
            show bambam happy
            bam "แฮ่! ทำไมมานั่งคนเดียวเนี่ย"
            p "!!!"
            p "แบม...ตกใจหมดเลย"
            hide bambam happy
            hide bambam normal
            show gao talk
            kao "แหมๆ ไหนบอกว่าจะอยู่กับพวกเราไง ทำไมถึงหนีมานั่งคนเดียวแบบนี้ล่ะ"
            kao "แล้วนี่เห็นมีนบ้างมั้ย"
            hide gao talk
            show gao normal
            p "อืม... ไม่เห็นเลยนะ"
            hide bambam talk
            show bambam sad
            bam "เห้อ ยัยมีนนี่จริงๆ เลยนะ เผลอแป๊บเดียวก็หลงทางกันซะได้"
            hide gao normal
            show gao talk
            kao "บางทีมีนอาจจะอยากกินข้าวคนเดียวก็ได้นะ"
            hide bambam sad
            hide gao talk
            show gao normal
            bam "ถ้าเพราะอย่างนั้นจริงๆ ก็ค่อยหายห่วงนิดนึงแหละนะ"

    scene toilet with dissolve
    play music "washing.mp3" noloop
    narrator "เสียงหยดน้ำเบาๆ ในอ่างล้างมือ"
    narrator "มีนกำลังล้างมืออย่างตั้งใจ ไม่ได้สนใจสิ่งรอบข้าง"
    narrator "ประตูห้องน้ำถูกผลักเปิดดัง ปัง!"
    narrator "แองจี้เดินเข้ามาท่าทางกราดเกรี้ยว"
    show angie talk at right
    angie "เจอกันจนได้นะ...มีน"
    narrator "มีนสะดุ้งหันมามองด้วยหน้าที่เริ่มซีด"
    hide angie talk 
    show angie normal at right
    show meen normal at left
    meen "อ..แองจี้ มีอะไรหรอ"
    show angie talk at right
    angie "อย่ามาทำเป็นไม่รู้น่า วันนี้แกทำฉันขายหน้าในห้องเรียน จำได้มั้ย"
    show meen talk at left
    meen "เราไม่ได้ตั้งใจเลยนะ..."
    show angie angry at right
    angie "ไม่ได้ต้ังใจเหรอ? พอมีคนมาปกป้องปุ๊บ ก็ทำตัวน่าสงสาร"
    angie "เก่งนักนะ เรื่องที่ทำให้คนอื่นสงสารไปทั่ว! น่าสมเพชชะมัด.."
    show meen talk at left
    meen "ไม่จริงเลยนะ...เราไม่เคยอยากให้ใครมาปกป้องเลย เราอยากอยู่เงียบๆ ด้วยซ้ำ..."
    show angie angry at right
    angie "เงียบ? ถ้าเงียบจริงๆ เธอคงไม่ทำตัวให้ครูเข้าข้างหรือให้เพื่อนมาแทรกกลางให้ฉันขายหน้าแบบนั้นหรอก!"
    show meen talk at left
    meen "เราไม่เคยคิดจะทำให้แองจี้ขายหน้าเลย...ถ้าเธอรู้สึกแบบนั้น เราขอโทษ แต่-"
    show angie angry at right
    angie "หุบปาก! ขอโทษหรอ? คำพูดตลกสิ้นดี"
    angie "มีน เธอรู้มั้ย ว่าคนอย่างเธอน่ารำคาญแค่ไหน?"
    narrator "แองจี้คว้ามือถือของมีนโยนลงพื้นดัง ปึก! มีนรีบก้มเก็บมือสั่น"
    show meen sad at left
    meen "แองจี้...เราก็เป็นเพื่อนกันมาตั้งแต่มอต้นนะ ทำไมต้องทำแบบนี้ด้วย..."
    narrator "แองจี้ชะงักพักหนึ่ง ก่อนแค่นหัวเราะเยาะกลบเกลื่อน"
    show angie angry at right
    angie "เพื่อน?"
    show angie talk at right
    angie "อย่ามาพูดให้ขำหน่อยเลย"
    angie "ฉันไม่เคยมองเธอเป็นเพื่อนซักนิด มองเป็นแค่ตัวถ่วงที่ดีแต่ทำให้ฉันอายต่อหน้าคนอื่น!"
    narrator "บรรยากาศเริ่มกดดันหนักขึ้น แองจี้จ้องเขม็งเข้ามาใกล้จนมีนถอยหนังติดผนังห้องน้ำ"
    show angie angry at right
    angie "จำไว้...อย่าทำให้ฉันเสียหน้าอีก ไม่งั้น..." 
    narrator "แองจี้ฟาดมือตบไปที่แก้มมีนเต็มแรง"
    play music "slap.mp3" noloop
    narrator "เพี๊ยะ!"
    narrator "เสียงก้องในห้องน้ำเงียบสงัด"
    show meen sad at left
    meen "อ...แองจี้ เราเจ็บนะ..."
    show angie angry at right
    angie "เจ็บสิดี เธอจะได้จำ"
    narrator "แองจี้หันหลังแล้วเดินออกไปพร้อมหัวเราะเย็นๆ"
    show angie angry at right
    angie "อ่อ อย่าเอาไปฟ้องใครล่ะ ไม่งั้นเธอโดนดีแน่"
    angie "แล้วจำคำฉันไว้นะมีน อย่าทำให้ฉันขายหน้าอีก"
    narrator "ประตูปิดลง ทิ้งมีนยืนสะอื้นอยู่คนเดียว น้ำตาไหลลงแก้ม"

    scene in_class with dissolve
    p "ทำไมมีนยังไม่กลับมาจากห้องน้ำอีกนะ..."
    bam "ยัยมีนหายไปไหนเนี่ย อย่าบอกนะว่ายัยนั่นคิดจะโดดเรียนตั้งแต่วันแรกเลยน่ะ"
    kao "เธอจะบ้าหรอ อย่างมีนนี่นะจะโดดเรียน"
    p "หรือจะเกิดขึ้นอะไรกับมีนนะ..."


    scene park_background with dissolve
    narrator "หลังเลิกเรียน คุณเห็นมีนเดินออกจากโรงเรียนคนเดียว ผ่านซอยเล็กๆ ที่ค่อนข้างเงียบ"
    menu:
        "คุณจะทำยังไง?"
        "ตะโกนเรียกมีน":
            $ trust_meen += 1
            p "เฮ้ มีน! รอด้วย เดี๋ยวเราเดินไปด้วย!"
            meen "หือ? อื้ม...ได้สิ"
        "ส่งข้อความหามีน":
            $ trust_meen += 1
            narrator "คุณส่งข้อความไปหาเขาในแอปโรงเรียน เธออ่านข้อความแล้วยิ้มเล็ก ๆ"
        "มองดูแล้วเดินกลับเอง":
            narrator "คุณมองดูเขาเดินหายไป แล้วเดินขึ้นรถเมล์กลับบ้านตามปกติ"

    scene bedroom_night with fade
    stop music fadeout 1.0
    play music "bgm_reflection.ogg"
    narrator "คืนนั้น คุณเขียนไดอารี่สั้น ๆ..."
    p "วันนี้เป็นวันแรกของโรงเรียนใหม่...แต่ในใจฉันบอกว่า..."
    p "ถ้าเราทำอะไรสักอย่างได้จริง ๆ...โรงเรียนนี้อาจจะเปลี่ยนไปก็ได้"


label episode_2:
    scene in_class with fade
    play music "background music.mp3" fadein 1.0
    narrator "เช้าวันจันทร์หลังเปิดเทอม มีนไม่ได้มาโรงเรียน"
    show bambam worry
    bam "นั่นน่ะ...ไม่น่าจะใช่แค่นั้นนะ"
    p "เกิดอะไรขึ้นหรอ"
    bam "ก็มีนน่ะสิ..."
    show gao normal at left
    kao "เอาจริง ๆ พวกเราควรไปดูเขาหน่อยไหม?"
    menu:
        "คุณจะทำยังไง?"
        "ไปหามีนที่บ้าน":
            jump visit_meen_home
        "รอให้มีนกลับมาเอง":
            jump wait_for_meen
        "บอกครูประจำชั้นให้ช่วยดู":
            jump tell_teacher

label visit_meen_home:
    scene meen_home with dissolve
    narrator "คุณและเก้าเดินทางไปบ้านมีนในตอนเย็น"
    meen_mom "สวัสดีค่ะ...มีนไม่ค่อยสบายและก็...เขาไม่ได้อยากเจอใครตอนนี้ค่ะ"
    bam "เรามาเป็นห่วงมีนค่ะ"
    narrator "แต่มีนยังไม่พร้อมจะพูดกับใคร"
    menu:
        "จะทำอย่างไรดี?"
        "ฝากข้อความดี ๆ ไว้ให้มีน":
            $ trust_meen += 1
            narrator "คุณเขียนข้อความให้กำลังใจมีนไว้ที่โต๊ะ"
            jump end_visit
        "บอกให้แม่มีนบอกมีนว่าคุณจะรอ":
            $ trust_meen += 1
            narrator "แม่มีนรับปากว่าจะบอกต่อ"
            jump end_visit

label end_visit:
    narrator "คุณรู้สึกว่า แม้ไม่ได้เจอมีนโดยตรง แต่เธอรู้ว่ามีคนเป็นห่วง"
    return

label wait_for_meen:
    narrator "คุณเลือกที่จะรอและสังเกตพฤติกรรมรอบตัวในโรงเรียน"
    bam "บางครั้งเสียงที่ไม่มีใครได้ยิน...คือเสียงที่ดังที่สุด"
    menu:
        "อยากจะทำอะไรต่อ?"
        "ลองพูดคุยกับเพื่อนคนอื่น ๆ เพื่อทำความเข้าใจ":
            jump talk_with_others
        "เก็บข้อมูลความรู้สึกของตัวเองในไดอารี่":
            jump write_diary

label tell_teacher:
    teacher "ขอบคุณที่บอกค่ะ ฉันจะลองติดต่อกับผู้ปกครองมีนดู"
    narrator "ครูประจำชั้นเริ่มใส่ใจปัญหาของมีนมากขึ้น"
    $ trust_meen += 1
    return

label talk_with_others:
    scene classroom with dissolve
    kao "รู้ไหม ว่ามีนโดนบอสกับแองจี้ล้อหนักมากในกลุ่ม"
    bam "มันถึงเวลาที่เราต้องทำอะไรสักอย่าง"
    menu:
        "จะทำยังไง?"
        "ยืนหยัดพูดความจริง":
            $ trust_bam += 1
            p "เราไม่ยอมให้มีนโดนบูลลี่แบบนี้อีกต่อไป"
            boss "ฮึ่ย จะทำอะไรได้ล่ะ?"
        "พยายามหลีกเลี่ยงความขัดแย้ง":
            p "อืม ก็...ขอเวลาอีกหน่อยนะ"
            bam "แบบนี้มันไม่ดีนะ"
    return

label write_diary:
    narrator "คุณจดบันทึกความรู้สึกของตัวเอง"
    p "วันนี้ได้เห็นว่า...เสียงเงียบ ๆ มันหนักหนาแค่ไหน"
    p "ถ้าเราไม่ช่วย มันอาจไม่มีใครได้ยินเลยจริง ๆ"
    return