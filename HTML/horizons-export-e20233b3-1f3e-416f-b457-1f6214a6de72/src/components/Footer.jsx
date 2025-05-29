
import React from "react";
import { motion } from "framer-motion";
import { Button } from "@/components/ui/button";
import { 
  Mail, 
  MapPin, 
  Phone,
  Twitter,
  Linkedin,
  Instagram,
  Github
} from "lucide-react";

const Footer = () => {
  const footerLinks = [
    {
      title: "Producto",
      links: [
        { name: "Características", href: "#features" },
        { name: "Precios", href: "#pricing" },
        { name: "Testimonios", href: "#testimonials" },
        { name: "Guías", href: "#" },
        { name: "API", href: "#" }
      ]
    },
    {
      title: "Empresa",
      links: [
        { name: "Sobre Nosotros", href: "#" },
        { name: "Carreras", href: "#" },
        { name: "Blog", href: "#" },
        { name: "Prensa", href: "#" },
        { name: "Socios", href: "#" }
      ]
    },
    {
      title: "Recursos",
      links: [
        { name: "Documentación", href: "#" },
        { name: "Tutoriales", href: "#" },
        { name: "Webinars", href: "#" },
        { name: "Centro de Ayuda", href: "#" },
        { name: "Comunidad", href: "#" }
      ]
    },
    {
      title: "Legal",
      links: [
        { name: "Privacidad", href: "#" },
        { name: "Términos", href: "#" },
        { name: "Cookies", href: "#" },
        { name: "Licencias", href: "#" },
        { name: "Configuración", href: "#" }
      ]
    }
  ];
  
  const socialLinks = [
    { icon: <Twitter className="h-5 w-5" />, href: "#", label: "Twitter" },
    { icon: <Linkedin className="h-5 w-5" />, href: "#", label: "LinkedIn" },
    { icon: <Instagram className="h-5 w-5" />, href: "#", label: "Instagram" },
    { icon: <Github className="h-5 w-5" />, href: "#", label: "GitHub" }
  ];
  
  const contactInfo = [
    { icon: <Mail className="h-5 w-5 text-indigo-400" />, text: "info@flowsaas.com" },
    { icon: <Phone className="h-5 w-5 text-indigo-400" />, text: "+34 91 123 4567" },
    { icon: <MapPin className="h-5 w-5 text-indigo-400" />, text: "Calle Innovación, 42, Madrid" }
  ];

  return (
    <footer id="footer" className="pt-20 pb-10 relative overflow-hidden">
      <div className="container mx-auto px-4">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mb-16">
          <div className="lg:col-span-1">
            <motion.div 
              className="text-2xl font-bold gradient-text mb-4"
              whileHover={{ scale: 1.05 }}
              transition={{ type: "spring", stiffness: 400, damping: 10 }}
            >
              FlowSaaS
            </motion.div>
            <p className="text-foreground/70 mb-6 max-w-md">
              Simplificamos los flujos de trabajo empresariales con nuestra plataforma SaaS intuitiva y potente, diseñada para equipos modernos.
            </p>
            
            <div className="space-y-3 mb-6">
              {contactInfo.map((item, index) => (
                <div key={index} className="flex items-center">
                  {item.icon}
                  <span className="ml-3 text-foreground/80">{item.text}</span>
                </div>
              ))}
            </div>
            
            <div className="flex space-x-4">
              {socialLinks.map((link, index) => (
                <motion.a
                  key={index}
                  href={link.href}
                  aria-label={link.label}
                  className="h-10 w-10 rounded-full bg-secondary/80 flex items-center justify-center text-foreground/80 hover:text-foreground transition-colors"
                  whileHover={{ scale: 1.1, backgroundColor: "rgba(79, 70, 229, 0.2)" }}
                  transition={{ type: "spring", stiffness: 400, damping: 10 }}
                >
                  {link.icon}
                </motion.a>
              ))}
            </div>
          </div>
          
          <div className="lg:col-span-2">
            <div className="grid grid-cols-2 md:grid-cols-4 gap-8">
              {footerLinks.map((group, groupIndex) => (
                <div key={groupIndex}>
                  <p className="font-medium text-foreground mb-4">{group.title}</p>
                  <ul className="space-y-3">
                    {group.links.map((link, linkIndex) => (
                      <li key={linkIndex}>
                        <a 
                          href={link.href} 
                          className="text-foreground/70 hover:text-foreground transition-colors"
                        >
                          {link.name}
                        </a>
                      </li>
                    ))}
                  </ul>
                </div>
              ))}
            </div>
          </div>
        </div>
        
        <div className="glass-card p-8 rounded-xl mb-16">
          <div className="flex flex-col md:flex-row items-center justify-between">
            <div className="mb-6 md:mb-0 md:mr-8 max-w-lg">
              <p className="font-medium text-xl mb-2">¿Listo para transformar tu flujo de trabajo?</p>
              <p className="text-foreground/80">
                Únete a miles de empresas que ya están optimizando sus procesos con nuestra plataforma.
              </p>
            </div>
            <div className="flex flex-col sm:flex-row gap-4">
              <Button className="bg-gradient-to-r from-indigo-500 via-purple-500 to-blue-500 hover:from-indigo-600 hover:via-purple-600 hover:to-blue-600 text-white px-6">
                Comenzar Gratis
              </Button>
              <Button variant="outline" className="border-white/20 hover:bg-white/10 px-6">
                Solicitar Demo
              </Button>
            </div>
          </div>
        </div>
        
        <div className="border-t border-white/10 pt-8 flex flex-col md:flex-row justify-between items-center">
          <p className="text-foreground/60 text-sm mb-4 md:mb-0">
            © 2025 FlowSaaS. Todos los derechos reservados.
          </p>
          <div className="flex flex-wrap gap-4 justify-center">
            <a href="#" className="text-foreground/60 hover:text-foreground text-sm transition-colors">
              Política de Privacidad
            </a>
            <a href="#" className="text-foreground/60 hover:text-foreground text-sm transition-colors">
              Términos de Servicio
            </a>
            <a href="#" className="text-foreground/60 hover:text-foreground text-sm transition-colors">
              Cookies
            </a>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
