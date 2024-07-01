# Expanding AIRO to allow for recording / documentation of bias
This repository contains the files associated with my MSc research project, supervised by Prof. David Lewis from Trinity College Dublin.

This project expands upon an existing open ontology, AIRO (https://github.com/DelaramGlp/airo). AIRO is an ontology for AI risk management in accordance with the EU AI Act. Expansions provide properties and types, also building upon DCAT and EARL, allowing for audits to be represented, with a particular focus on managing bias, as is required by the European Union's AI Act. A mapping from these biases to potential EU fundamental right violations is also provided, which functions to assist with AI Act compliance.

Using recursive properties (allowing for the range of a property to match its domain), audits which are conducted may be documented for each stage in an AI system's development pipeline. An AI system may be described in terms of its component AI systems. Each AI system may have machine learning models (`airo:MLModel`) as components. 

Recursive querying is then possible using SPARQL, allowing for information to be obtained about audits conducted on a particular AI system's foundation model, for example, significantly aiding in modelling the risks in downstream AI systems. In principle, this could be any model or system which is upstream from the system presently being modelled using AIRO. This is particularly important with the emerging foundation model paradigm in machine learning (see, e.g., https://link.springer.com/article/10.1007/s12599-024-00851-0).

