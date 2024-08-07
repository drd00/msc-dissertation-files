package com.example;
import java.io.StringWriter;

import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdf.model.Resource;
import org.apache.jena.riot.RDFDataMgr;
import org.topbraid.shacl.validation.ValidationUtil;
import org.topbraid.shacl.vocabulary.SH;

public class App {
    private static void checkCompliance(String datagraphPath, String shapeGraphPath, String classDefinitionsPath) {
        Model dataGraph = RDFDataMgr.loadModel(datagraphPath);
        Model shapeGraph = RDFDataMgr.loadModel(shapeGraphPath);
        Model classDefinitions = RDFDataMgr.loadModel(classDefinitionsPath);

        dataGraph.add(classDefinitions);
        Resource report = ValidationUtil.validateModel(dataGraph, shapeGraph, true);
        System.out.println(report.getModel().write(new StringWriter(), "TURTLE"));
        boolean conforms = report.getProperty(SH.conforms).getBoolean();
        System.out.println("Conforms: " + conforms);
    }

    public static void main(String[] args) {
        System.out.println("Checking compliance of datagraph with SHACL shape for the CheXpert dataset...");
        checkCompliance("rdf/use-case-chexpert.ttl", "rdf/datasheets-shapes.ttl", "rdf/datasheets-dcat-dqv.ttl");

        System.out.println("Checking compliance of datagraph with SHACL shape for the Movie review polarity dataset...");
        checkCompliance("rdf/use-case-moview-review.ttl", "rdf/datasheets-shapes.ttl", "rdf/datasheets-dcat-dqv.ttl");
    }
}
