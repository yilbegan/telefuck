from telefuck.brainfuck import Brainfuck


def test_interpreter():
    code = """
    ++++++++[>++++[>++>+++>+++>+<<<<-]>+>->+>>+[<]<-]>>.
    >>---.+++++++..+++.>.<<-.>.+++.------.--------.>+.
    """  # Hello world
    fuck = Brainfuck(code)
    result = fuck.evaluate(limit=1000)
    assert result == "Hello World!"
