#!/usr/bin/env python

from manimlib.imports import *

class Deret(Scene):
    def construct(self):
        basel = TexMobject("\\frac{1}{1\\cdot 2}+\\frac{1}{2\\cdot 3}+\\frac{1}{3\\cdot4}+...+\\frac{1}{9\\cdot10}")
        text = TextMobject("Evaluate the sum of the series above")
        group1 = VGroup(basel, text).arrange(DOWN)
        self.play(
            FadeIn(basel),
            Write(text)
        )
        self.wait()

        self.play(LaggedStart(*map(FadeOutAndShiftDown, group1)))
        self.wait()

        text2 = TextMobject("Lets first analyze the series of the denominator")
        basel2 = TexMobject("(1\\cdot 2)\\quad (2\\cdot 3)\\quad (3\\cdot 4)\\quad (4\\cdot 5)\\quad (5\\cdot 6) \\quad ...")
        basel2.shift(DOWN)
        basel2_2 = TexMobject("2\\quad", "6\\quad", "12\\quad", "20\\quad", "30","\\quad ...")
        basel2_2.shift(DOWN)
        group2 = VGroup(text2, basel2).arrange(DOWN)
        self.play(
            Write(text2),
            FadeIn(basel2)
        )
        self.wait()
        self.play(ReplacementTransform(basel2, basel2_2))
        self.wait()

        frame1 = SurroundingRectangle(basel2_2[0:2], buff=.1)
        frame2 = SurroundingRectangle(basel2_2[1:3], buff=.1)
        frame3 = SurroundingRectangle(basel2_2[2:4], buff=.1)
        frame4 = SurroundingRectangle(basel2_2[3:5], buff=.1)
        frame5 = SurroundingRectangle(basel2_2[4:], buff=.1)
        const1 = TextMobject("The differences are\\\\4")
        const1.next_to(frame1, DOWN)
        const2 = TextMobject("The differences are\\\\6")
        const2.next_to(frame2, DOWN)
        const3 = TextMobject("The differences are\\\\8")
        const3.next_to(frame3, DOWN)
        const4 = TextMobject("The differences are\\\\10")
        const4.next_to(frame4, DOWN)
        const5 = TextMobject("And so on")
        const5.next_to(frame5, DOWN)
        self.play(ShowCreation(frame1), FadeIn(const1))
        self.wait()
        self.play(
            ReplacementTransform(frame1, frame2),
            ReplacementTransform(const1, const2)
        )
        self.wait()
        self.play(
            ReplacementTransform(frame2, frame3),
            ReplacementTransform(const2, const3)
        )
        self.wait()
        self.play(
            ReplacementTransform(frame3, frame4),
            ReplacementTransform(const3, const4)
        )
        self.wait()
        self.play(
            ReplacementTransform(frame4, frame5),
            ReplacementTransform(const4, const5)
        )
        self.wait()

        self.play(LaggedStart(*map(FadeOutAndShiftDown, const5)), Uncreate(frame5))
        self.wait()

        basel3 = TexMobject("2\\quad", "6\\quad", "8\\quad", "10\\quad", "...")
        basel3.shift(DOWN)
        self.play(ReplacementTransform(basel2_2, basel3))
        self.wait()

        frame1_2 = SurroundingRectangle(basel3[0:2], buff=.1)
        frame2_2 = SurroundingRectangle(basel3[1:3], buff=.1)
        frame3_2 = SurroundingRectangle(basel3[2:4], buff=.1)
        frame4_2 = SurroundingRectangle(basel3[3:], buff=.1)
        const1_2 = TextMobject("The differences are\\\\2")
        const1_2.next_to(frame1_2, DOWN)
        const2_2 = TextMobject("The differences are\\\\2")
        const2_2.next_to(frame2_2, DOWN)
        const3_2 = TextMobject("The differences are\\\\2")
        const3_2.next_to(frame3_2, DOWN)
        const4_2 = TextMobject("And so on")
        const4_2.next_to(frame4_2, DOWN)
        self.play(ShowCreation(frame1_2), FadeIn(const1_2))
        self.wait()
        self.play(
            ReplacementTransform(frame1_2, frame2_2),
            ReplacementTransform(const1_2, const2_2)
        )
        self.wait()
        self.play(
            ReplacementTransform(frame2_2, frame3_2),
            ReplacementTransform(const2_2, const3_2)
        )
        self.wait()
        self.play(
            ReplacementTransform(frame3_2, frame4_2),
            ReplacementTransform(const3_2, const4_2)
        )
        self.wait()

        text3 = TextMobject("Since the difference constant at 2\\emph{nd} order\\\\so we're gonna use general equation for 2\\emph{nd} order arithmetic series")
        text3.scale(0.6)
        self.play(
            Uncreate(frame4_2),
            LaggedStart(*map(FadeOutAndShiftDown, basel3)),
            LaggedStart(*map(FadeOutAndShiftDown, const4_2))
        )
        self.wait()
        self.play(ReplacementTransform(text2, text3))
        self.wait()

        basel4 = TexMobject("U_n = an^2 + bn + c")
        text4 = TextMobject("Where n is the n\\emph{th} term of the series\\\\", "and a, b, and c are constants")
        text4.scale(0.5)
        text4.shift(DOWN)
        self.play(
            LaggedStart(*map(FadeOutAndShiftDown, text3)),
        )
        self.wait()
        self.play(
            Write(basel4),
            FadeInFromDown(text4[0])
        )
        self.wait()
        self.play(FadeInFromDown(text4[1]))
        self.wait()

        self.play(
            LaggedStart(*map(FadeOutAndShiftDown, basel4))
        )
        self.wait()

        text5 = TextMobject("From the equation before, we got")
        text5.shift(2*UP)
        basel5 = TexMobject("U_1 = a(1)^2 + b(1) + c\\\\", "U_2 = a(2)^2 + b(2) + c\\\\", "U_3 = a(3)^2 + b(3) + c\\\\.\\\\.\\\\.")
        basel5.shift(DOWN)
        self.play(
            ReplacementTransform(text4, text5)
        )
        self.wait()
        self.play(FadeInFromDown(basel5[0]))
        self.wait(0.5)
        self.play(FadeInFromDown(basel5[1]))
        self.wait(0.5)
        self.play(FadeInFromDown(basel5[2]))
        self.wait()

        basel5_2 = TexMobject("U_1 = a + b + c\\\\", "U_2 = 4a + 2b + c\\\\", "U_3 = 9a +3b +c\\\\.\\\\.\\\\.")
        basel5_2.shift(DOWN)
        self.play(ReplacementTransform(basel5[0], basel5_2[0]))
        self.wait()
        self.play(ReplacementTransform(basel5[1], basel5_2[1]))
        self.wait()
        self.play(ReplacementTransform(basel5[2], basel5_2[2]))
        self.wait()

        text6 = TextMobject("The difference equation for the 1\\emph{st} order")
        text6.shift(UP)
        basel6 = TexMobject("b_{11} = U_2 - U_1 = 3a + b\\\\", "b_{12} = U_3 - U_2 = 5a+b\\\\",".\\\\.\\\\.\\\\")
        basel6.shift(DOWN)
        self.play(LaggedStart(*map(FadeOutAndShiftDown, basel5_2)))
        self.wait()
        self.play(ReplacementTransform(text5, text6))
        self.wait()
        self.play(FadeIn(basel6))
        self.wait()

        self.play(LaggedStart(*map(FadeOutAndShiftDown, basel6)))
        self.wait()

        text7 = TextMobject("The difference equation for the 2\\emph{nd} order")
        text7.shift(UP)
        basel7 = TexMobject("b_{21} = b_{12}-b_{11} = 2a\\\\",".\\\\.\\\\.")
        basel7.shift(DOWN)
        self.play(ReplacementTransform(text6, text7))
        self.wait()
        self.play(FadeIn(basel7))
        self.wait()

        self.play(LaggedStart(*map(FadeOutAndShiftDown, text7)), LaggedStart(*map(FadeOutAndShiftDown, basel7)))
        self.wait()

        texto = TexMobject(
            "1\\cdot 2",
            "2\\cdot 3",
            "3\\cdot 4",
            "4\\cdot 5",
            "5\\cdot 6"
        )
        texto2 = TexMobject(
            "2",
            "6",
            "12",
            "20",
            "30",
            "4",
            "6",
            "8",
            "10",
            "2",
            "2",
            "2"
        )
        texto3 = TexMobject(
            "a+b+c\\quad",
            "4a+2b+c\\quad",
            "9a+3b+c\\quad",
            "16a+4b+c\\quad",
            "25a+5b+c"
        )
        texto4 = TexMobject("3a+b\\quad", "5a+b\\quad", "7a+b\\quad", "9a+b")
        texto5 = TexMobject("2a\\quad","2a\\quad","2a")
        VGroup(texto3, texto4, texto5).arrange(DOWN)
        texto[0].shift(4*LEFT+2*UP)
        texto[1].shift(2*LEFT + 2*UP)
        texto[2].shift(2*UP)
        texto[3].shift(2*RIGHT + 2*UP)
        texto[4].shift(4*RIGHT + 2*UP)
        texto2[0].shift(np.array([-4,2,0]))
        texto2[1].shift(np.array([-2,2,0]))
        texto2[2].shift(np.array([0,2,0]))
        texto2[3].shift(np.array([2,2,0]))
        texto2[4].shift(np.array([4,2,0]))
        texto2[5].next_to(texto2[0:2], 2*DOWN)
        texto2[6].next_to(texto2[1:3], 2*DOWN)
        texto2[7].next_to(texto2[2:4], 2*DOWN)
        texto2[8].next_to(texto2[3:5], 2*DOWN)
        texto2[9].next_to(texto2[5:7], 2*DOWN)
        texto2[10].next_to(texto2[6:8], 2*DOWN)
        texto2[11].next_to(texto2[7:9], 2*DOWN)
        texto3.scale(0.7)
        self.play(
            FadeInFromDown(texto)
        )
        self.wait()
        self.play(
            ReplacementTransform(texto, texto2[0:5])
        )
        self.wait()
        self.play(
            ReplacementTransform(texto2[0:2].copy() ,texto2[5]),
            ReplacementTransform(texto2[1:3].copy(), texto2[6]),
            ReplacementTransform(texto2[2:4].copy(), texto2[7]),
            ReplacementTransform(texto2[3:5].copy(), texto2[8])
        )
        self.wait()
        self.play(
            ReplacementTransform(texto2[5:7].copy() ,texto2[9]),
            ReplacementTransform(texto2[6:8].copy(), texto2[10]),
            ReplacementTransform(texto2[7:9].copy(), texto2[11])
        )
        self.wait()
        self.play(
            ReplacementTransform(texto2[0:5], texto3)
        )
        self.wait(0.4)
        self.play(
            ReplacementTransform(texto2[5] ,texto4[0]),
            ReplacementTransform(texto2[6], texto4[1]),
            ReplacementTransform(texto2[7], texto4[2]),
            ReplacementTransform(texto2[8], texto4[3])
        )
        self.wait(0.4)
        self.play(
            ReplacementTransform(texto2[9] ,texto5[0]),
            ReplacementTransform(texto2[10], texto5[1]),
            ReplacementTransform(texto2[11], texto5[2])
        )
        self.wait(0.4)

        frame6 = SurroundingRectangle(texto3[0], buff=.1)
        frame7 = SurroundingRectangle(texto4[0], buff=.1)
        frame8 = SurroundingRectangle(texto5[0], buff=.1)
        text8 = TextMobject("We're gonna use these equation for solving a, b, and c")
        text8.to_corner(RIGHT + DOWN)
        self.play(
            ShowCreation(frame6),
            ShowCreation(frame7),
            ShowCreation(frame8),
            Write(text8)
        )
        self.wait()

        self.play(
            LaggedStart(*map(FadeOutAndShiftDown, text8)),
            LaggedStart(*map(FadeOutAndShiftDown, texto3)),
            LaggedStart(*map(FadeOutAndShiftDown, texto4)),
            LaggedStart(*map(FadeOutAndShiftDown, texto5)),
            Uncreate(frame6),
            Uncreate(frame7),
            Uncreate(frame8)
        )
        self.wait()

        text9 = TextMobject("We know that")
        text9.shift(UP)
        text9_2 = TextMobject("So")
        text9_2.shift(UP)
        basel8 = TexMobject("2a = 2")
        basel8_2 = TexMobject("a = 1")
        self.play(FadeInFromDown(text9), Write(basel8))
        self.wait()
        self.play(ReplacementTransform(basel8, basel8_2), ReplacementTransform(text9, text9_2))
        self.wait()

        self.play(LaggedStart(*map(FadeOutAndShiftDown, basel8_2)), LaggedStart(*map(FadeOutAndShiftDown, text9_2)))
        self.wait()

        basel9 = TexMobject("3a+b = 4")
        basel9_2 = TexMobject("3(1)+b = 4")
        basel9_3 = TexMobject("b = 4-3")
        basel9_4 = TexMobject("b=1")
        text10 = TextMobject("Substitute a from equation before")
        text10.shift(2*DOWN)
        self.play(
            FadeInFromDown(basel9),
        )
        self.wait(0.5)
        self.play(FadeInFromDown(text10))
        self.wait()
        self.play(LaggedStart(*map(FadeOutAndShiftDown, text10)), ReplacementTransform(basel9, basel9_2))
        self.wait()
        self.play(ReplacementTransform(basel9_2, basel9_3))
        self.wait()
        self.play(ReplacementTransform(basel9_3, basel9_4))
        self.wait()

        self.play(LaggedStart(*map(FadeOutAndShiftDown, basel9_4)))
        self.wait()

        basel10 = TexMobject("a+b+c=2")
        basel10_2 = TexMobject("(1)+(1)+c=2")
        basel10_3 = TexMobject("2+c=2")
        basel10_4 = TexMobject("c=0")
        text11 = TextMobject("Substitute a and b from equation before")
        text11.shift(2*DOWN)
        self.play(FadeInFromDown(basel10))
        self.wait(0.5)
        self.play(FadeInFromDown(text11))
        self.wait()
        self.play(LaggedStart(*map(FadeOutAndShiftDown, text11)), ReplacementTransform(basel10, basel10_2))
        self.wait()
        self.play(ReplacementTransform(basel10_2, basel10_3))
        self.wait()
        self.play(ReplacementTransform(basel10_3, basel10_4))
        self.wait()

        self.play(LaggedStart(*map(FadeOutAndShiftDown, basel10_4)))
        self.wait()

        basel11 = TexMobject("a=1\\\\b=1\\\\c=0")
        basel11.shift(0.5*DOWN)
        text12 = TextMobject("Now we got our constants")
        text12.shift(UP)
        text12_2 = TextMobject("Lets put it back to our equation")
        text12_2.shift(UP)
        self.play(FadeInFromDown(text12), FadeInFromDown(basel11))
        self.wait()
        self.play(ReplacementTransform(text12, text12_2))
        self.wait()

        self.play(LaggedStart(*map(FadeOutAndShiftDown, text12_2)), LaggedStart(*map(FadeOutAndShiftDown, basel11)))
        self.wait()

        basel12 = TexMobject("U_n = an^2 + bn + c")
        basel12_2 = TexMobject("U_n = (1)n^2 + (1)n + (0)")
        basel12_3 = TexMobject("U_n = n^2 + n")
        basel12_4 = TexMobject("U_n = n(n+1)")
        basel12_5 = TexMobject("U_n = \\frac{1}{n(n+1)}")
        text13 = TextMobject("Now we got general pattern for the series")
        text13.shift(2*DOWN)
        self.play(FadeInFromDown(basel12))
        self.wait()
        self.play(ReplacementTransform(basel12, basel12_2))
        self.wait()
        self.play(ReplacementTransform(basel12_2, basel12_3))
        self.wait()
        self.play(ReplacementTransform(basel12_3, basel12_4))
        self.wait()
        self.play(ReplacementTransform(basel12_4, basel12_5), FadeIn(text13))
        self.wait()

        self.play(LaggedStart(*map(FadeOutAndShiftDown, text13)), LaggedStart(*map(FadeOutAndShiftDown, basel12_5)))
        self.wait()

        text14 = TextMobject("Now we have to find the equation for the sum of the series")
        text14.shift(UP)
        basel13 = TexMobject("S_n = \\frac{1}{1\\cdot 2} + \\frac{1}{2\\cdot 3} + ... + \\frac{1}{n(n+1)}")
        basel13_2 = TexMobject("S_n = \\frac{2-1}{1\\cdot 2} + \\frac{3-2}{2\\cdot 3} + ... + \\frac{(n+1)-n}{n(n+1)}")
        basel13_3 = TexMobject("S_n = \\frac{2}{1\\cdot 2} - \\frac{1}{1\\cdot 2} + \\frac{3}{2\\cdot 3} - \\frac{2}{2\\cdot 3} + ... + \\frac{n+1}{n(n+1)}-\\frac{n}{n(n+1)}")
        basel13_4 = TexMobject("S_n = 1 -", "\\frac{1}{2}+ \\frac{1}{2}- \\frac{1}{3} + ... \\frac{n+1}{n(n+1)}","+ \\frac{n}{n(n+1)}")
        basel13_5 = TexMobject("S_n = 1 - \\frac{n}{n(n+1)}")
        frame9 = SurroundingRectangle(basel13_4[1], buff=.1)
        const6 = TexMobject("0")
        const6.next_to(frame9, DOWN)
        self.play(Write(text14))
        self.wait()
        self.play(FadeInFromDown(basel13))
        self.wait()
        self.play(ReplacementTransform(basel13, basel13_2))
        self.wait()
        self.play(ReplacementTransform(basel13_2, basel13_3))
        self.wait()
        self.play(ReplacementTransform(basel13_3, basel13_4))
        self.wait()
        self.play(ShowCreation(frame9), FadeInFromDown(const6))
        self.wait()
        self.play(Uncreate(frame9), LaggedStart(*map(FadeOutAndShiftDown, const6)))
        self.wait()
        self.play(ReplacementTransform(basel13_4, basel13_5))
        self.wait()

        text15 = TextMobject("Simplify the equation")
        text15.shift(UP)
        text15_2 = TextMobject("So we got")
        text15_2.shift(UP)
        basel14 = TexMobject("S_n = \\frac{n}{n+1}")
        self.play(
            LaggedStart(*map(FadeOutAndShiftDown, text14)),
            LaggedStart(*map(FadeOutAndShiftDown, basel13_5)),
            FadeIn(text15)
        )
        self.wait()
        self.play(ReplacementTransform(text15, text15_2), FadeInFromDown(basel14))
        self.wait()

        self.play(LaggedStart(*map(FadeOutAndShiftDown, basel14)), LaggedStart(*map(FadeOutAndShiftDown, text15_2)))
        self.wait()

        text16 = TextMobject("Now we can easily calculate the sum of the series")
        text16.shift(UP)
        basel14_2 = TexMobject("S_n = \\frac{9}{9+1}")
        basel14_3 = TexMobject("S_n = \\frac{9}{10}")
        basel14_4 = TexMobject("S_n = 0.9")
        self.play(FadeIn(text16), Write(basel))
        self.wait()
        self.play(ReplacementTransform(basel, basel14))
        self.wait()
        self.play(ReplacementTransform(basel14, basel14_2))
        self.wait()
        self.play(ReplacementTransform(basel14_2, basel14_3))
        self.wait()
        self.play(ReplacementTransform(basel14_3, basel14_4))
        self.wait(2)

        self.play(LaggedStart(*map(FadeOutAndShiftDown, text16)), LaggedStart(*map(FadeOutAndShiftDown, basel14_4)))
        self.wait()

        last_text = TexMobject("\\int", "M","a","t","h db")
        last_text[1].set_color(RED_E)
        last_text[3].set_color(RED_E)
        self.play(Write(last_text))
        self.wait()
