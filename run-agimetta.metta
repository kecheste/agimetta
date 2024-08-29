! (import! &self agimetta)
 ;; run the news agent
! (news "Tesla")
 ;; run the sentiment analysis agent
! (sentiment "Tesla is revolutionizing the electric vehicle market with innovative technology.")
 ;; run the output of the news agent to the running space knoweldge
! (add-reduct &self (news "Tesla"))
 ;; read the knowledges present in the running space
! (match &self $x $x)
