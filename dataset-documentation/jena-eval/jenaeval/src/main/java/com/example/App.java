package com.example;
import java.io.StringWriter;

import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdf.model.Resource;
import org.apache.jena.riot.RDFDataMgr;
import org.topbraid.shacl.validation.ValidationUtil;
import org.topbraid.shacl.vocabulary.SH;

public class App 
{
    public static void main( String[] args )
    {
        System.out.println( "Checking compliance of datagraph with SHACL shape..." );
        
        Model dataGraph = RDFDataMgr.loadModel("rdf/use-case-chexpert.ttl");
        Model shapeGraph = RDFDataMgr.loadModel("rdf/datasheets-shapes.ttl");
        Model classDefinitions = RDFDataMgr.loadModel("rdf/datasheets-dcat-dqv.ttl");

        dataGraph.add(classDefinitions);

        Resource report = ValidationUtil.validateModel(dataGraph, shapeGraph, true);

        System.out.println(report.getModel().write(new StringWriter(), "TURTLE"));

        boolean conforms = report.getProperty(SH.conforms).getBoolean();
        System.out.println("Conforms: " + conforms);
    }
}
