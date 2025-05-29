
import React from "react";
import { motion } from "framer-motion";
import { Toaster } from "@/components/ui/toaster";
import { Button } from "@/components/ui/button";
import { useToast } from "@/components/ui/use-toast";
import Hero from "@/components/Hero";
import Features from "@/components/Features";
import Pricing from "@/components/Pricing";
import Testimonials from "@/components/Testimonials";
import Footer from "@/components/Footer";
import Navbar from "@/components/Navbar";

function App() {
  const { toast } = useToast();

  const handleDemoRequest = () => {
    toast({
      title: "Solicitud recibida",
      description: "Nos pondremos en contacto contigo pronto para agendar una demostración.",
    });
  };

  return (
    <div className="min-h-screen bg-gradient-to-b from-background to-background/95 overflow-hidden">
      <Navbar />
      <Hero onDemoRequest={handleDemoRequest} />
      <Features />
      <Pricing />
      <Testimonials />
      <Footer />
      <Toaster />
    </div>
  );
}

export default App;
