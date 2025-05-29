
import React, { useState } from "react";
import { motion } from "framer-motion";
import { Button } from "@/components/ui/button";
import { Check, X } from "lucide-react";

const Pricing = () => {
  const [isAnnual, setIsAnnual] = useState(true);
  
  const plans = [
    {
      name: "Básico",
      description: "Ideal para individuos y pequeños equipos",
      monthlyPrice: 19,
      annualPrice: 190,
      features: [
        "Hasta 3 usuarios",
        "10 proyectos",
        "5GB de almacenamiento",
        "Automatizaciones básicas",
        "Soporte por email"
      ],
      notIncluded: [
        "Análisis avanzados",
        "Integraciones personalizadas",
        "Soporte prioritario"
      ],
      cta: "Comenzar Gratis",
      popular: false
    },
    {
      name: "Profesional",
      description: "Perfecto para equipos en crecimiento",
      monthlyPrice: 49,
      annualPrice: 490,
      features: [
        "Hasta 10 usuarios",
        "Proyectos ilimitados",
        "50GB de almacenamiento",
        "Automatizaciones avanzadas",
        "Análisis en tiempo real",
        "Integraciones API",
        "Soporte prioritario"
      ],
      notIncluded: [
        "Personalización completa",
        "Implementación dedicada"
      ],
      cta: "Comenzar Prueba Gratuita",
      popular: true
    },
    {
      name: "Empresarial",
      description: "Solución completa para grandes organizaciones",
      monthlyPrice: 99,
      annualPrice: 990,
      features: [
        "Usuarios ilimitados",
        "Proyectos ilimitados",
        "Almacenamiento ilimitado",
        "Automatizaciones personalizadas",
        "Análisis avanzados",
        "Integraciones personalizadas",
        "Soporte 24/7",
        "Implementación dedicada",
        "SLA garantizado"
      ],
      notIncluded: [],
      cta: "Contactar Ventas",
      popular: false
    }
  ];
  
  const containerVariants = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: {
        staggerChildren: 0.2
      }
    }
  };
  
  const itemVariants = {
    hidden: { opacity: 0, y: 20 },
    visible: {
      opacity: 1,
      y: 0,
      transition: { duration: 0.5, ease: "easeOut" }
    }
  };

  return (
    <section id="pricing" className="py-20 relative overflow-hidden">
      <div className="container mx-auto px-4">
        <motion.div 
          className="text-center max-w-3xl mx-auto mb-16"
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
        >
          <span className="inline-block px-4 py-2 rounded-full bg-indigo-500/10 text-indigo-400 text-sm font-medium mb-4">
            Precios
          </span>
          <h2 className="mb-6">
            <span className="gradient-text">Planes flexibles</span> para cada necesidad
          </h2>
          <p className="text-lg text-foreground/80 mb-8">
            Elige el plan que mejor se adapte a tus necesidades. Todos los planes incluyen acceso a nuestras funcionalidades principales.
          </p>
          
          <div className="flex items-center justify-center mb-8">
            <span className={`mr-3 ${!isAnnual ? 'text-foreground' : 'text-foreground/60'}`}>Mensual</span>
            <button
              onClick={() => setIsAnnual(!isAnnual)}
              className="relative inline-flex h-6 w-12 items-center rounded-full bg-secondary transition-colors focus:outline-none"
              role="switch"
              aria-checked={isAnnual}
            >
              <span
                className={`${
                  isAnnual ? 'translate-x-6' : 'translate-x-1'
                } inline-block h-4 w-4 transform rounded-full bg-indigo-500 transition-transform`}
              />
            </button>
            <span className={`ml-3 flex items-center ${isAnnual ? 'text-foreground' : 'text-foreground/60'}`}>
              Anual <span className="ml-2 text-xs px-2 py-1 bg-indigo-500/20 text-indigo-400 rounded-full">Ahorra 20%</span>
            </span>
          </div>
        </motion.div>
        
        <motion.div 
          variants={containerVariants}
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true }}
          className="grid grid-cols-1 md:grid-cols-3 gap-8"
        >
          {plans.map((plan, index) => (
            <motion.div 
              key={index} 
              variants={itemVariants}
              className={`pricing-card relative ${plan.popular ? 'border-indigo-500/50' : 'border-white/10'}`}
              whileHover={{ y: -5, boxShadow: "0 10px 30px -10px rgba(79, 70, 229, 0.2)" }}
            >
              {plan.popular && (
                <div className="absolute top-0 right-0 -mt-2 -mr-2">
                  <span className="inline-block px-3 py-1 bg-gradient-to-r from-indigo-500 to-purple-500 text-white text-xs font-medium rounded-full">
                    Más Popular
                  </span>
                </div>
              )}
              
              <h3 className="text-xl font-bold mb-2">{plan.name}</h3>
              <p className="text-foreground/70 mb-6">{plan.description}</p>
              
              <div className="mb-6">
                <span className="text-4xl font-bold">
                  ${isAnnual ? plan.annualPrice : plan.monthlyPrice}
                </span>
                <span className="text-foreground/70">
                  {isAnnual ? '/año' : '/mes'}
                </span>
              </div>
              
              <Button 
                className={`w-full mb-8 ${
                  plan.popular 
                    ? 'bg-gradient-to-r from-indigo-500 via-purple-500 to-blue-500 hover:from-indigo-600 hover:via-purple-600 hover:to-blue-600 text-white' 
                    : 'bg-secondary hover:bg-secondary/80'
                }`}
              >
                {plan.cta}
              </Button>
              
              <div className="space-y-3">
                <p className="font-medium text-sm text-foreground/80 mb-2">Incluye:</p>
                {plan.features.map((feature, i) => (
                  <div key={i} className="flex items-start">
                    <Check className="h-5 w-5 text-indigo-400 mr-3 mt-0.5 flex-shrink-0" />
                    <span className="text-foreground/80 text-sm">{feature}</span>
                  </div>
                ))}
                
                {plan.notIncluded.length > 0 && (
                  <>
                    <p className="font-medium text-sm text-foreground/80 mt-4 mb-2">No incluye:</p>
                    {plan.notIncluded.map((feature, i) => (
                      <div key={i} className="flex items-start">
                        <X className="h-5 w-5 text-foreground/40 mr-3 mt-0.5 flex-shrink-0" />
                        <span className="text-foreground/60 text-sm">{feature}</span>
                      </div>
                    ))}
                  </>
                )}
              </div>
            </motion.div>
          ))}
        </motion.div>
        
        <motion.div 
          className="mt-16 text-center"
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          viewport={{ once: true }}
          transition={{ delay: 0.4 }}
        >
          <p className="text-foreground/80 mb-4">
            ¿Necesitas una solución personalizada para tu empresa?
          </p>
          <Button variant="outline" className="border-white/20 hover:bg-white/10">
            Contacta con nuestro equipo de ventas
          </Button>
        </motion.div>
      </div>
    </section>
  );
};

export default Pricing;
