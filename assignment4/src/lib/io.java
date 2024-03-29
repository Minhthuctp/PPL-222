import java.io.*;
import java.io.IOException;

// import bkool.codegeneration.IllegalRuntimeException;

public class io {
  // private static final DataInputStream input = new
  // DataInputStream(System.in);
  public static BufferedReader input =
      new BufferedReader(new InputStreamReader(System.in));
  public static Writer writer =
      new BufferedWriter(new OutputStreamWriter(System.out));

  // public io(String name) throws IOException {

  // }

  /**
   * reads and returns an integer value from the standard input
   *
   * @return int an integer number read from standard input
   */
  public static int readInteger() {
    String tmp = "";
    try {
      tmp = input.readLine();
      return Integer.parseInt(tmp);
    } catch (IOException e) {
      e.printStackTrace();
    } catch (NumberFormatException e) {
      e.printStackTrace();
    }
    return 0;
  }

  /**
   * print out the value of the integer i to the standard output
   *
   * @param i the value is printed out
   */
  public static void printInteger(int i) { System.out.print(i + "\n"); }

  /**
   * same as printInteger except that it also prints a newline
   *
   * @param i the value is printed out
   */
  public static void printIntegerLn(int i) { System.out.println(i + "\n"); }

  /**
   * return a floating-point value read from the standard input
   *
   * @return float the floating-point value
   */
  public static float readFloat() {
    String tmp = "";
    try {
      tmp = input.readLine();
      return Float.parseFloat(tmp);
    } catch (IOException e) {
      e.printStackTrace();
      ;
    } catch (NumberFormatException e) {
      e.printStackTrace();
      ;
    }
    return 0.0F;
  }

  /**
   * print out the value of the float f to the standard output
   *
   * @param f the floating-point value is printed out
   */
  public static void writeFloat(float f) { System.out.print(f + "\n"); }

  /**
   * same as writeFloat except that it also prints a newline
   *
   * @param f the floating-point value is printed out
   */
  public static void writeFloatLn(float f) { System.out.println(f + "\n"); }

  /**
   * reads and returns a boolean value from the standard input
   *
   * @return int a boolean value read from standard input
   */
  public static boolean readBoolean() {
    String tmp = "";
    try {
      tmp = input.readLine();
      if (tmp.equalsIgnoreCase("true"))
        return true;
      else // if (tmp.equalsIgnoreCase("false"))
        return false;
      // else throw new IllegalRuntimeException(tmp);
    } catch (IOException e) {
      e.printStackTrace();
    }
    return false;
  }

  /**
   * print out the value of the boolean b to the standard output
   *
   * @param b the boolean value is printed out
   */
  public static void printBoolean(boolean b) { System.out.print(b + "\n"); }

  /**
   * same as printBoolean except that it also prints a new line
   *
   * @param b the boolean value is printed out
   */
  public static void printBooleanLn(boolean b) { System.out.println(b + "\n"); }

  /**
   * return a string value read from the standard input
   *
   * @return string value
   */
  public static String readString() {
    String tmp = "";
    try {
      tmp = input.readLine();
      return tmp;
    } catch (IOException e) {
      e.printStackTrace();
      ;
    }
    return tmp;
  }

  /**
   * prints the value of the string to the standard output
   *
   * @param a the string is printed out
   */
  public static void printString(String a) { System.out.print(a); }

  /**
   * same as putString except that it also prints a new line
   *
   * @param a the string is printed out
   */
  public static void printStringLn(String a) { System.out.println(a); }

  public static void close() {
    try {
      writer.close();
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}