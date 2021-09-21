#/bin/python3

# code from https://calmcode.io/typer/commands.html
import typer

app = typer.Typer(name="demo", add_completion=False, help="This is a demo app.")

@app.command()
def hello_world(name):
    """Say hello"""
    print(f"hello {name}!")

@app.command()
def goodbye_world(name):
    """Say goodbye"""
    print(f"goodbye {name}!")

@app.command()
def meow():
    '''Say meow'''
    print("MEOW")

@app.command()
def time():
    '''Print utc time'''
    import datetime
    utc_time = datetime.datetime.utcnow() 
    print(utc_time.strftime('%Y/%m/%d %H:%M:%S'))

@app.command()
def seqcnt(path):
    '''Print number of sequences in fasta file'''
    seqcnt = 0
    with open(path, "r") as inf:
        for line in inf:
            if ">" in line:
                seqcnt += 1
    print(seqcnt)

if __name__ == "__main__":
    app()
