
import React, { useRef } from "react";
import { motion, useInView } from "framer-motion";
import { Star } from "lucide-react";

const Testimonials = () => {
  const ref = useRef(null);
  const isInView = useInView(ref, { once: true, amount: 0.2 });
  
  const testimonials = [
    {
      name: "Ana Rodríguez",
      role: "Directora de Operaciones, TechCorp",
      image: "ana-rodriguez",
      quote: "Desde que implementamos esta plataforma, nuestra productividad ha aumentado un 35%. La interfaz intuitiva y las potentes automatizaciones han transformado completamente nuestros flujos de trabajo.",
      stars: 5
    },
    {
      name: "Carlos Méndez",
      role: "Fundador, StartupVision",
      image: "carlos-mendez",
      quote: "Como startup en crecimiento, necesitábamos una solución que creciera con nosotros. Esta plataforma nos ha proporcionado exactamente eso, con una escalabilidad impresionante y un soporte excepcional.",
      stars: 5
    },
    {
      name: "Elena Torres",
      role: "Gerente de Proyectos, DesignStudio",
      image: "elena-torres",
      quote: "Las herramientas de colaboración han mejorado significativamente la comunicación entre nuestros equipos distribuidos. Ahora completamos proyectos en la mitad del tiempo que antes.",
      stars: 4
    },
    {
      name: "Javier Morales",
      role: "Director de Tecnología, InnovaSoft",
      image: "javier-morales",
      quote: "La integración con nuestras herramientas existentes fue perfecta. El panel de análisis nos proporciona insights valiosos que nos ayudan a tomar decisiones más informadas.",
      stars: 5
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
    <section id="testimonials" className="py-20 relative overflow-hidden">
      <div className="container mx-auto px-4">
        <motion.div 
          className="text-center max-w-3xl mx-auto mb-16"
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
        >
          <span className="inline-block px-4 py-2 rounded-full bg-indigo-500/10 text-indigo-400 text-sm font-medium mb-4">
            Testimonios
          </span>
          <h2 className="mb-6">
            <span className="gradient-text">Lo que dicen</span> nuestros clientes
          </h2>
          <p className="text-lg text-foreground/80">
            Descubre cómo nuestra plataforma ha ayudado a empresas de todos los tamaños a optimizar sus operaciones y alcanzar sus objetivos.
          </p>
        </motion.div>
        
        <motion.div 
          ref={ref}
          variants={containerVariants}
          initial="hidden"
          animate={isInView ? "visible" : "hidden"}
          className="grid grid-cols-1 md:grid-cols-2 gap-8"
        >
          {testimonials.map((testimonial, index) => (
            <motion.div 
              key={index} 
              variants={itemVariants}
              className="testimonial-card"
              whileHover={{ y: -5, boxShadow: "0 10px 30px -10px rgba(79, 70, 229, 0.2)" }}
            >
              <div className="flex items-center mb-4">
                <div className="mr-4 rounded-full overflow-hidden w-12 h-12 bg-indigo-500/20 flex items-center justify-center">
                  <img  alt={`Foto de perfil de ${testimonial.name}`} className="w-full h-full object-cover" src="https://images.unsplash.com/photo-1598932324015-91232f2bca84" />
                </div>
                <div>
                  <h4 className="font-bold">{testimonial.name}</h4>
                  <p className="text-sm text-foreground/70">{testimonial.role}</p>
                </div>
              </div>
              
              <div className="flex mb-4">
                {[...Array(5)].map((_, i) => (
                  <Star 
                    key={i} 
                    className={`h-4 w-4 ${i < testimonial.stars ? 'text-yellow-400 fill-yellow-400' : 'text-foreground/30'}`} 
                  />
                ))}
              </div>
              
              <p className="text-foreground/80 italic">"{testimonial.quote}"</p>
            </motion.div>
          ))}
        </motion.div>
        
        <motion.div 
          className="mt-16 p-8 glass-card rounded-xl max-w-4xl mx-auto"
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ delay: 0.4 }}
        >
          <div className="flex flex-col md:flex-row items-center">
            <div className="mb-6 md:mb-0 md:mr-8 md:w-1/3">
              <img  alt="Logotipos de empresas que confían en nosotros" className="w-full" src="https://images.unsplash.com/photo-1658203897456-14cdc8e81146" />
            </div>
            <div className="md:w-2/3">
              <h3 className="text-2xl font-bold mb-4">Más de 500 empresas confían en nosotros</h3>
              <p className="text-foreground/80 mb-6">
                Desde startups hasta grandes corporaciones, ayudamos a empresas de todos los tamaños a optimizar sus operaciones y alcanzar sus objetivos.
              </p>
              <div className="flex flex-wrap gap-3">
                <span className="px-3 py-1 bg-indigo-500/10 text-indigo-400 rounded-full text-sm">Tecnología</span>
                <span className="px-3 py-1 bg-purple-500/10 text-purple-400 rounded-full text-sm">Finanzas</span>
                <span className="px-3 py-1 bg-blue-500/10 text-blue-400 rounded-full text-sm">Salud</span>
                <span className="px-3 py-1 bg-indigo-500/10 text-indigo-400 rounded-full text-sm">Educación</span>
                <span className="px-3 py-1 bg-purple-500/10 text-purple-400 rounded-full text-sm">E-commerce</span>
              </div>
            </div>
          </div>
        </motion.div>
      </div>
    </section>
  );
};

export default Testimonials;
