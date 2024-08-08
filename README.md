# Improving transparency and representating bias reports in open knowledge graphs
This repository contains the files associated with my MSc research project, supervised by Prof. David Lewis from Trinity College Dublin.

This project expands upon an existing open ontology, AIRO (https://github.com/DelaramGlp/airo). Expansions provide properties and classes, expanding upon EARL and utilising DQV and DCAT, allowing for bias tests and relevant documentation, such as datasheets, to be represented. As the EU AI Act places a significant emphasis on mitigating biases which may harm an individual's fundamental rights, a mapping from societal biases (which may be represented as bias test results) onto potential EU fundamental right violations is provided, which functions to assist with AI Act compliance.

Using recursive properties (allowing for the range of a property to match its domain), audits which are conducted may be documented for each stage in an AI system's development pipeline. An AI system may be described in terms of its component models, which may further specify component models (for example, in the case that a model is a fine-tuned variant of an upstream model). 
