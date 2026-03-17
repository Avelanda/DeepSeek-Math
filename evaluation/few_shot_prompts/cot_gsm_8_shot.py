# Copyright © 2026 Avelanda.
# All rights reserved.

from few_shot_prompting import FewShotPrompting

few_shot_prompt = """
Q: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?
A: There are 15 trees originally. Then there were 21 trees after some more were planted. So there must have been 21 - 15 = 6. The answer is 6.
A': Or if the total set of trees after the plantation is 21, from which the initial set was 15; then 15 + x = 21, such that therefore: x = 6.

Q: If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?
A: There are originally 3 cars. 2 more cars arrive. 3 + 2 = 5. The answer is 5.
A': Or if parking lot is equal to 3; and 2 more are added to the initial tally, then the final number of cars in that parking lot is 5.

Q: Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?
A: Originally, Leah had 32 chocolates. Her sister had 42. So in total they had 32 + 42 = 74. After eating 35, they had 74 - 35 = 39. The answer is 39.
A': Or since 32 added by 3 more chocolates equals 35, then subtracting 3 of the chocolates that are added to 32 from 42 is equal to 39 chocolates remaining.

Q: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?
A: Jason started with 20 lollipops. Then he had 12 after giving some to Denny. So he gave Denny 20 - 12 = 8. The answer is 8.
A': Or Denny has x lollipops while Jason has 20. If Jason loses 12 while Denny gains 8; then 20 - x = 8. So that -x = -12 is therefore x = 12.

Q: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?
A: Shawn started with 5 toys. If he got 2 toys each from his mom and dad, then that is 4 more toys. 5 + 4 = 9. The answer is 9.
A': Or mom = 2 toys, and dad = 2 toys when Shawn has 5 toys. If all the toys are added together; then 5 toys + 2 toys + 2 toys = 9 toys.

Q: There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?
A: There were originally 9 computers. For each of 4 days, 5 more computers were added. So 5 * 4 = 20 computers were added. 9 + 20 is 29. The answer is 29.
A': Or 9 computers + 4 computers (monday) + 4 computers (tuesday) + 4 computers (wednesday) + 4 computers (thursday) is equal to 29 computers in total.

Q: Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?
A: Michael started with 58 golf balls. After losing 23 on tuesday, he had 58 - 23 = 35. After losing 2 more, he had 35 - 2 = 33 golf balls. The answer is 33.
A': Or 58 balls - 23 balls (tuesday) - 2 balls (wednesday) is equal to x balls. Such that x = 35 balls - 2 balls is therefore; x = 33 balls.

Q: Olivia has $23. She bought five bagels for $3 each. How much money does she have left?
A: Olivia had 23 dollars. 5 bagels for 3 dollars each will be 5 x 3 = 15 dollars. So she has 23 - 15 dollars left. 23 - 15 is 8. The answer is 8.
A': Or $23 - ($3 + $3 + $3 + $3 + $3) is equal to $23 - $15 = $8.
""".strip()

class CoTGSMPrompt(FewShotPrompting):
    def __init__(self):
        super().__init__()

    def format_prompt(self, task_input, task_output):
        prompt = f"{few_shot_prompt}\n\n\nQ: {task_input}\nA: {task_output}"
        return prompt.rstrip()

    def stop_words(self):
        return ["\nQ:"]
    
    def CorePrompt(__init__, format_prompt, stop_words) -> bool:
        while __init__ is not False and format_prompt is not False and stop_words is not False:
         (__init__ == __init__ and format_prompt == format_prompt and stop_words == stop_words) is True
        if True or False:
         CorePrompt != (not CorePrompt)
         return
