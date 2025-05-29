
import React from "react";
import { motion } from "framer-motion";
import { Button } from "@/components/ui/button";
import { ArrowRight, CheckCircle } from "lucide-react";

const Hero = ({ onDemoRequest }) => {
  const container = {
    hidden: { opacity: 0 },
    show: {
      opacity: 1,
      transition: {
        staggerChildren: 0.2,
      },
    },
  };

  const item = {
    hidden: { opacity: 0, y: 20 },
    show: { opacity: 1, y: 0, transition: { duration: 0.6, ease: "easeOut" } },
  };

  const benefits = [
    "Automatización de flujos de trabajo",
    "Colaboración en tiempo real",
    "Análisis avanzados",
    "Integraciones personalizadas",
  ];

  return (
    <section className="relative pt-32 pb-20 overflow-hidden hero-gradient">
      <div className="blob blob-purple"></div>
      <div className="blob blob-blue"></div>
      
      <div className="container mx-auto px-4">
        <motion.div
          className="max-w-4xl mx-auto text-center"
          variants={container}
          initial="hidden"
          animate="show"
        >
          <motion.div variants={item} className="mb-6">
            <span className="inline-block px-4 py-2 rounded-full bg-indigo-500/10 text-indigo-400 text-sm font-medium mb-4">
              Plataforma Todo-en-Uno
            </span>
          </motion.div>
          
          <motion.h1 variants={item} className="mb-6">
            <span className="gradient-text">Simplifica tu flujo de trabajo</span> con nuestra plataforma SaaS
          </motion.h1>
          
          <motion.p variants={item} className="text-xl text-foreground/80 mb-8 max-w-2xl mx-auto">
            Optimiza tus procesos, mejora la colaboración y aumenta la productividad con nuestra solución integral para equipos modernos.
          </motion.p>
          
          <motion.div variants={item} className="flex flex-col sm:flex-row justify-center gap-4 mb-12">
            <Button className="bg-gradient-to-r from-indigo-500 via-purple-500 to-blue-500 hover:from-indigo-600 hover:via-purple-600 hover:to-blue-600 text-white px-8 py-6 h-auto text-lg">
              Comenzar Gratis
              <ArrowRight className="ml-2 h-5 w-5" />
            </Button>
            <Button variant="outline" className="border-white/20 hover:bg-white/10 px-8 py-6 h-auto text-lg" onClick={onDemoRequest}>
              Solicitar Demo
            </Button>
          </motion.div>
          
          <motion.div variants={item} className="flex flex-wrap justify-center gap-x-8 gap-y-4">
            {benefits.map((benefit, index) => (
              <div key={index} className="flex items-center">
                <CheckCircle className="h-5 w-5 text-indigo-400 mr-2" />
                <span className="text-foreground/80">{benefit}</span>
              </div>
            ))}
          </motion.div>
        </motion.div>
        
        <motion.div
          variants={item}
          className="mt-16 relative"
          initial={{ opacity: 0, y: 40 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.6 }}
        >
          <div className="glass-card p-2 sm:p-4 rounded-xl overflow-hidden shadow-xl">
            <div className="aspect-[16/9] rounded-lg overflow-hidden bg-gradient-to-br from-indigo-900/40 via-purple-900/40 to-blue-900/40 flex items-center justify-center">
              <img  alt="Dashboard de la plataforma SaaS mostrando análisis y estadísticas" className="w-full h-full object-cover" src="https://images.unsplash.com/photo-1686061594225-3e92c0cd51b0" />
            </div>
          </div>
          <div className="absolute -inset-0.5 bg-gradient-to-r from-indigo-500 via-purple-500 to-blue-500 rounded-xl blur opacity-20 -z-10"></div>
        </motion.div>
      </div>
    </section>
  );
};

export default Hero;
