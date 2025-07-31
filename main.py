from test_case_generator import nlp_parser, rules_engine, test_case_writer

with open("examples/sample_requirements.txt") as file:
    requirements_text = file.read()

sentences = nlp_parser.extract_sentences(requirements_text)
test_cases = rules_engine.generate_test_cases(sentences)
test_case_writer.write_to_csv(test_cases, "output/test_cases.csv")
