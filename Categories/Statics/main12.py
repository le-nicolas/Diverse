from manim import *

class VectorDecomposition3D(ThreeDScene):
    def construct(self):
        # Setting up the 3D axes
        axes = ThreeDAxes()

        # Define the vectors (in 3D space)
        vector1 = np.array([2, 3, 5])
        vector2 = np.array([1, 0, 4])
        force = np.array([4, 2, 1])

        # Normalize vector2 for parallel component calculation
        vector2_unit = vector2 / np.linalg.norm(vector2)

        # Parallel and perpendicular components of the force relative to vector2
        force_parallel = np.dot(force, vector2_unit) * vector2_unit
        force_perpendicular = force - force_parallel

        # Create the vectors using Manim's `Arrow3D` objects
        vector1_arrow = Arrow3D(start=[0, 0, 0], end=vector1, color=BLUE)
        vector2_arrow = Arrow3D(start=[0, 0, 0], end=vector2, color=RED)
        force_arrow = Arrow3D(start=[0, 0, 0], end=force, color=GREEN)
        force_parallel_arrow = Arrow3D(start=[0, 0, 0], end=force_parallel, color=ORANGE)
        force_perpendicular_arrow = Arrow3D(start=[0, 0, 0], end=force_perpendicular, color=PURPLE)

        # Add 3D axes
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.play(Create(axes))

        # "Before" scene: show original vectors and the force
        self.play(Create(vector1_arrow), Create(vector2_arrow), Create(force_arrow))
        self.wait(2)

        # Transition to "After": Show the decomposition
        self.play(Transform(force_arrow, force_parallel_arrow))
        self.play(Create(force_perpendicular_arrow))
        self.wait(2)

        # Hold the scene for a moment
        self.wait(2)

        # End the scene
        self.play(FadeOut(vector1_arrow), FadeOut(vector2_arrow), FadeOut(force_parallel_arrow), FadeOut(force_perpendicular_arrow), FadeOut(axes))


# a code that makes its own animation via manim and ffmpeg
# manim is a library for animation.. vscode setups the code via documentation and root it to the path...which is the ffmpeg/bin.

