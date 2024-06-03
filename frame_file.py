'''
NAME: frame_file.py 

VERSION: 3

AUTHOR: Santiago Orozco        

DESCRIPTION: script que genera 6 archivos, uno para cada marco de lectura de una archivo con secuencia de DNA

USAGE
    % python frame_file.py <archivo.txt>
    % python frame_file.py <archivo.txt>

positional arguments:
  input_file            Nombre del archivo con la secuencia de nucleótidos

options:
  -h, --help            show this help message and exit



METHOD
    1. Se toma un archivo desde línea de comandos en formato string.
    2. Crea y abre un archivo en formato de escritura
    3. Escribe desntro del archivo cada codón separado por un espacio
    4. Cada 10 codones se escribe un salto de línea
    5. Se repiten los pasos 2-4 para los marcos de lectura del 1 al 3
    6. Se saca el inverso complementario de la secuencia del archivo
    7. Se repiten los pasos 2-4 para los marcos de lectura restantes, del 4 al 6
'''
from Bio .Seq import Seq
import re
import argparse
from Bio import SeqIO

def generate_codon_file(name_file, seqobj):
    with open(name_file, "a") as archivo:
        archivo.write("\n>\n")
        j = 0
        for codon in re.findall(r"(.{3})", str(seqobj)):
            archivo.write(f"{codon} ")
            j += 1
            if j == 10:
                archivo.write("\n")
                j = 0

parser = argparse.ArgumentParser(description="Lee archivo de entrada y salida")

parser.add_argument("input_file", type=str, help="El archivo de texto que quieres procesar.")
args = parser.parse_args()

#with open(args.input_file, "r") as f:
    #ADN = f.read().upper() 
#seqobj = Seq(ADN)
for l in range(1,6):
    new_file = "Frame_" + str(l)
    with open(new_file, "w"):
        pass

for seq in SeqIO.parse(args.input_file, "fasta"):
    seqobj = seq.seq
    frame = 0
    k = 0
    while frame <= 5:
        if frame == 3:
            seqobj = seqobj.reverse_complement()
            k = 0
        seq = seqobj[k:]
        # print(f"frame{frame+1} is {seq}")
        file = "Frame_" + str(frame + 1)
        generate_codon_file(file, seq)
        frame += 1
        k += 1


