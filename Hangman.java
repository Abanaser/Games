import java.util.Random;
import java.util.Scanner;
public class Hangman {
    public Scanner input = new Scanner(System.in);
    Random rnd = new Random();
    private String[] words = {"cat","car","test","air","book","sky"}; // These words are up to you to change
    private char[] hiddenWord;
    private char[] guessedWord;
    private int numOfMiss=0;
    public Hangman() {
        char[] hiddenWord;
        char[] guessedWord;

    }
    private char gWord = ' ';

    public String[] getWords() {
        return words;
    }

    public char[] getHiddenWord() {
        return hiddenWord;
    }

    private int indexOf(char c) {
        for(int i =0; i<hiddenWord.length;i++) {
            if(hiddenWord[i]==c)
                return i;
        }
        return -1;
    }

    private void setCharAt(int i,char c,char[] arr) {arr[i] = c;}

    private String pickWord() {
        int bound =  rnd.nextInt(words.length);
        return words[bound];
    }

    private char[] copyStringToArray(String s) {
        return s.toCharArray();
    }

    private void printWord() {
        System.out.print(guessedWord);
    }

    private boolean isComplete() {
        for(int i=0;i<guessedWord.length;i++ )
            if(guessedWord[i]=='*')
                return false;
        return true;
    }

    private void playOneRound() {
        hiddenWord= copyStringToArray(pickWord());
        guessedWord= new char[hiddenWord.length];
        for(int i =0;i<guessedWord.length;i++)
            guessedWord[i]= '*';
        do {
            System.out.print("(Guess) Enter a letter in word ");
            printWord();
            System.out.print(" >");
            char gWord = input.next().charAt(0);
            if(indexOf(gWord)==-1) {
                if(isExist(gWord))
                    System.out.println(gWord + " Is already in the world.");
                else {
                    System.out.println(gWord + " Is not in the word.");
                    numOfMiss++;

                }
            }else {
                for(int i = 0; i<hiddenWord.length ;i++)
                    if(indexOf(gWord)!=-1) {
                        setCharAt(indexOf(gWord), gWord, guessedWord);
                        setCharAt(indexOf(gWord),'$', hiddenWord);
                    }

            }

        }while(!isComplete());
    }
    private boolean isExist(char c) {
        for(int i = 0 ; i < guessedWord.length ; i++) {
            if(c == guessedWord[i])
                return true;
        }
        return false;
    }

    public void play() {
        int numOfPlays=0;
        char ans= ' ';
        do {
            numOfMiss=0;
            if(numOfPlays==0) {
                System.out.println("Welcome to Hangman game. Are you ready? OK, let us start:");
                playOneRound();
                System.out.print("The word is ");
                printWord();
                System.out.println(". You missed "+numOfMiss+" time ");
                numOfPlays++;
            }
            else {
                System.out.print("Do you want to guess another word? Enter y or n>");
                ans = input.next().charAt(0);
                switch(ans) {
                    case 'n':
                        System.out.println("Goodbye!");
                        break;
                    case 'y':
                        playOneRound();
                        System.out.print("The word is ");
                        printWord();
                        System.out.println(". You missed "+numOfMiss+" time ");
                        break;
                }
            }
        }while(ans!='n');
    }

    public static void main(String[] args) {
        Hangman game = new Hangman();
        game.play();
    }

}

