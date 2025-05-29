
import React, { useEffect, useRef } from "react";
import { motion, useAnimation, useInView } from "framer-motion";
import { 
  Zap, 
  BarChart3, 
  Users, 
  Lock, 
  Layers, 
  Smartphone 
} from "lucide-react";

const Features = () => {
  const controls = useAnimation();
  const ref = useRef(null);
  const isInView = useInView(ref, { once: true, amount: 0.2 });
  
  useEffect(() => {
    if (isInView) {
      controls.start("visible");
    }
  }, [controls, isInView]);
  
  const features = [
    {
      icon: <Zap className="h-10 w-10 text-indigo-400" />,
      title: "Automatización Inteligente",
      description: "Automatiza tareas repetitivas y flujos de trabajo complejos con nuestra tecnología de IA avanzada."
    },
    {
      icon: <BarChart3 className="h-10 w-10 text-purple-400" />,
      title: "Análisis en Tiempo Real",
      description: "Obtén insights valiosos con paneles personalizables y reportes detallados sobre el rendimiento."
    },
    {
      icon: <Users className="h-10 w-10 text-blue-400" />,
      title: "Colaboración Perfecta",
      description: "Trabaja sin problemas con tu equipo en tiempo real, sin importar dónde se encuentren."
    },
    {
      icon: <Lock className="h-10 w-10 text-indigo-400" />,
      title: "Seguridad Avanzada",
      description: "Protege tus datos con encriptación de nivel empresarial y controles de acceso granulares."
    },
    {
      icon: <Layers className="h-10 w-10 text-purple-400" />,
      title: "Integraciones Flexibles",
      description: "Conecta con tus herramientas favoritas a través de nuestra API robusta y extensible."
    },
    {
      icon: <Smartphone className="h-10 w-10 text-blue-400" />,
      title: "Experiencia Móvil",
      description: "Accede a todas las funcionalidades desde cualquier dispositivo con nuestra interfaz adaptable."
    }
  ];
  
  const containerVariants = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: {
        staggerChildren: 0.1
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
    <section id="features" className="py-20 relative overflow-hidden">
      <div className="container mx-auto px-4">
        <motion.div 
          className="text-center max-w-3xl mx-auto mb-16"
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
        >
          <span className="inline-block px-4 py-2 rounded-full bg-indigo-500/10 text-indigo-400 text-sm font-medium mb-4">
            Características
          </span>
          <h2 className="mb-6">
            <span className="gradient-text">Potentes funcionalidades</span> diseñadas para tu éxito
          </h2>
          <p className="text-lg text-foreground/80">
            Nuestra plataforma combina herramientas avanzadas con una interfaz intuitiva para ayudarte a alcanzar tus objetivos de manera eficiente.
          </p>
        </motion.div>
        
        <motion.div 
          ref={ref}
          variants={containerVariants}
          initial="hidden"
          animate={controls}
          className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8"
        >
          {features.map((feature, index) => (
            <motion.div 
              key={index} 
              variants={itemVariants}
              className="feature-card"
              whileHover={{ y: -5, boxShadow: "0 10px 30px -10px rgba(79, 70, 229, 0.2)" }}
            >
              <div className="mb-4">{feature.icon}</div>
              <h3 className="text-xl font-bold mb-3">{feature.title}</h3>
              <p className="text-foreground/80">{feature.description}</p>
            </motion.div>
          ))}
        </motion.div>
      </div>
    </section>
  );
};

export default Features;
