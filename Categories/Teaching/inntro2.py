from manim import *

class SpecificVolumeDifference(Scene):
    def construct(self):
        # Title
        title = Text("Specific Volume Comparison", font_size=48, color=BLUE).to_edge(UP)
        self.play(Write(title))
        
        # Define masses and specific volume text
        rock_mass = Text("1 kg Rock", font_size=36, color=GRAY).shift(2 * LEFT + UP)
        feather_mass = Text("1 kg Feather", font_size=36, color=GRAY).shift(2 * RIGHT + UP)
        
        # Specific volume formulas
        rock_specific_volume = MathTex("v_{rock} = \\frac{1 \\text{ m}^3}{1000 \\text{ kg}}", color=RED).next_to(rock_mass, DOWN)
        feather_specific_volume = MathTex("v_{feather} = \\frac{1 \\text{ m}^3}{1 \\text{ kg}}", color=GREEN).next_to(feather_mass, DOWN)
        
        # Objects representations
        rock = Circle(radius=0.5, color=RED, fill_opacity=0.6).next_to(rock_specific_volume, DOWN)
        feather = Circle(radius=2, color=GREEN, fill_opacity=0.4).next_to(feather_specific_volume, DOWN)
        
        # Play animations
        self.play(Write(rock_mass), Write(feather_mass))
        self.play(FadeIn(rock_specific_volume), FadeIn(feather_specific_volume))
        self.play(GrowFromCenter(rock), GrowFromCenter(feather))
        
        # Labels for visual scale (specific volumes)
        rock_label = Text("Small Volume", font_size=24, color=RED).next_to(rock, DOWN)
        feather_label = Text("Large Volume", font_size=24, color=GREEN).next_to(feather, DOWN)
        
        self.play(FadeIn(rock_label), FadeIn(feather_label))
        
        # Hold the final scene for a moment
        self.wait(2)
        
        # Fade out all
        self.play(FadeOut(title), FadeOut(rock_mass), FadeOut(feather_mass), FadeOut(rock_specific_volume), 
                  FadeOut(feather_specific_volume), FadeOut(rock), FadeOut(feather), FadeOut(rock_label), FadeOut(feather_label))
