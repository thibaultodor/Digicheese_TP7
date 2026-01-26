INSERT INTO `utilisateur` (`id`, `name`, `email`, `password`) VALUES
(1, 'admin', 'admin@gmail.com', 'scrypt:32768:8:1$Cyb2VwHqEYt1LaJo$3b50fc9a8f9588c97c477df972f130fcc639f87ffff7c609c5c090fdf88cc5d4ab55a8d21c4bb1eb38dbd25708bb9d866bf1cbe08f1db741733fdeab509f4e47'),
(10, 'colis', 'colis@gmail.com', 'scrypt:32768:8:1$t8SiXI09cqKMSGrC$33d27f1769ee85577f021580389fb524f0c6a45c49ed3ae950742fdbc562df6b8d3aac97e5b8baa5511179819ce06ea98ac04c0c2f80ee4a9ad61b5f0d5f599e'),
(14, 'Utildemomodif', 'utildemo@gmail.com', 'scrypt:32768:8:1$s8sKuqgOIcLU3tLt$beab3bf16f9241875b2f4393e07de12408d92f32663e8f2372af2c7f47428eee5b4a3473e58313981c5e77fe67681a78b30442ad1af469ea3692221323bed01b');
 
 
INSERT INTO `roles_utilisateur` (`user_id`, `role_id`) VALUES (1, 2), (10, 5);
 
INSERT INTO `role` (`id`, `libelle`) VALUES (2, 'admin'), (5, 'colis');
 