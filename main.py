from argparse import ArgumentParser
from qiskit import qasm2


gate_map = {
    'x': 'X',
    'y': 'Y',
    'z': 'Z',
    'cx': 'CNOT',
}


def main():
    # parsing command line arguments
    parser = ArgumentParser()
    parser.add_argument('input', type=str)
    parser.add_argument('-o', '--output', type=str)
    args = parser.parse_args()

    # parsing qasm file into qiskit circuit
    qc = qasm2.load(args.input, custom_instructions=qasm2.LEGACY_CUSTOM_INSTRUCTIONS)
    
    # Quipper header with type definition
    dpq_header = 'module QASMCirc where\nimport "lib/Prelude.dpq"\n'
    dpq_type = 'circ : ! (Vec Qubit %d -> (Vec Qubit %d, Vec Bit %d))' % (qc.num_qubits, qc.num_qubits, qc.num_clbits)

    # looping over gates and converting to quipper code
    dpq_circ_text = 'circ = \n\tlet '
    gate_strs = []
    for x in qc.data:
        breakpoint()


if __name__ == '__main__':
    main()
