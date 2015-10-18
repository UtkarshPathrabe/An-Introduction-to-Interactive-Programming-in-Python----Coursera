Lecture 04 Quiz
===============  

Question
--------  
Why should a blackjack hand and a deck of cards be implemented as two different classes?  

### Answer  
* They each have different behaviors.  
* You might reuse the deck class in a different card game. The hand is specific to blackjack.  

#### Explanation  
There are no hard and fast rules about what should and should not be implemented as a class. You need to think about how you are going to use (and reuse) the code that you are writing. When designing a class, you need to think about both the data and the behaviors (methods) the class will have.  