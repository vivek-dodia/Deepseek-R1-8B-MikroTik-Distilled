# Repository Information
Name: Easy-HotSpot

# Files

File: config
================================================
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://gitlab.com/audy018/Easy-HotSpot.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "Development"]
	remote = origin
	merge = refs/heads/Development
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: config.php
================================================
<?php 
$host = "192.168.1.123";
$user = "admin";
$pass = "admin";
?>
================================================

File: animate.css
================================================
.animated.delay-01 {
	animation-delay: 0s;
	-webkit-animation-delay: 0s;
	-moz-animation-delay: 0s;
	-o-animation-delay: 0s;
}
.animated.delay-02 {
	animation-delay: 0.5s;
	-webkit-animation-delay: 0.5s;
	-moz-animation-delay: 0.5s;
	-o-animation-delay: 0.5s;
}
.animated.delay-03 {
	animation-delay: 1s;
	-webkit-animation-delay: 1s;
	-moz-animation-delay: 1s;
	-o-animation-delay: 1s;
}
.animated.delay-04 {
	animation-delay: 1.5s;
	-webkit-animation-delay: 1.5s;
	-moz-animation-delay: 1.5s;
	-o-animation-delay: 1.5s;
}
.animated.delay-05 {
	animation-delay: 2s;
	-webkit-animation-delay: 2s;
	-moz-animation-delay: 2s;
	-o-animation-delay: 2s;
}
.animated.delay-06 {
	animation-delay: 2.5s;
	-webkit-animation-delay: 2.5s;
	-moz-animation-delay: 2.5s;
	-o-animation-delay: 2.5s;
}
.animated.delay-07 {
	animation-delay: 3s;
	-webkit-animation-delay: 3s;
	-moz-animation-delay: 3s;
	-o-animation-delay: 3s;
}
.animated.delay-08 {
	animation-delay: 3.5s;
	-webkit-animation-delay: 3.5s;
	-moz-animation-delay: 3.5s;
	-o-animation-delay: 3.5s;
}
.animated.delay-09 {
	animation-delay: 4s;
	-webkit-animation-delay: 4s;
	-moz-animation-delay: 4s;
	-o-animation-delay: 4s;
}
.animated.delay-10 {
	animation-delay: 4.5s;
	-webkit-animation-delay: 4.5s;
	-moz-animation-delay: 4.5s;
	-o-animation-delay: 4.5s;
}
.animated.delay-11 {
	animation-delay: 5s;
	-webkit-animation-delay: 5s;
	-moz-animation-delay: 5s;
	-o-animation-delay: 5s;
}
.animated.delay-12 {
	animation-delay: 5.5s;
	-webkit-animation-delay: 5.5s;
	-moz-animation-delay: 5.5s;
	-o-animation-delay: 5.5s;
}
.animated.delay-13 {
	animation-delay: 6s;
	-webkit-animation-delay: 6s;
	-moz-animation-delay: 6s;
	-o-animation-delay: 6s;
}
.animated.delay-14 {
	animation-delay: 6.5s;
	-webkit-animation-delay: 6.5s;
	-moz-animation-delay: 6.5s;
	-o-animation-delay: 6.5s;
}
.animated.delay-15 {
	animation-delay: 7s;
	-webkit-animation-delay: 7s;
	-moz-animation-delay: 7s;
	-o-animation-delay: 7s;
}
.animated.delay-16 {
	animation-delay: 7.5s;
	-webkit-animation-delay: 7.5s;
	-moz-animation-delay: 7.5s;
	-o-animation-delay: 7.5s;
}
.animated.delay-17 {
	animation-delay: 8s;
	-webkit-animation-delay: 8s;
	-moz-animation-delay: 8s;
	-o-animation-delay: 8s;
}
.animated.delay-18 {
	animation-delay: 8.5s;
	-webkit-animation-delay: 8.5s;
	-moz-animation-delay: 8.5s;
	-o-animation-delay: 8.5s;
}
.animated.delay-19 {
	animation-delay: 9s;
	-webkit-animation-delay: 9s;
	-moz-animation-delay: 9s;
	-o-animation-delay: 9s;
}
.animated.delay-20 {
	animation-delay: 9.5s;
	-webkit-animation-delay: 9.5s;
	-moz-animation-delay: 9.5s;
	-o-animation-delay: 9.5s;
}
.animated {
	-webkit-animation-duration: 1s;
	-moz-animation-duration: 1s;
	-o-animation-duration: 1s;
	animation-duration: 1s;
	-webkit-animation-fill-mode: both;
	   -moz-animation-fill-mode: both;
	     -o-animation-fill-mode: both;
	        animation-fill-mode: both;
}
.animated.hinge{
	-webkit-animation-duration:2s;
	-moz-animation-duration:2s;
	-ms-animation-duration:2s;
	-o-animation-duration:2s;
	animation-duration:2s;
}
@-webkit-keyframes flash {
	0%, 50%, 100% {opacity: 1;}	25%, 75% {opacity: 0;}
}
@-moz-keyframes flash {
	0%, 50%, 100% {opacity: 1;}	
	25%, 75% {opacity: 0;}
}
@-o-keyframes flash {
	0%, 50%, 100% {opacity: 1;}	
	25%, 75% {opacity: 0;}
}
@keyframes flash {
	0%, 50%, 100% {opacity: 1;}	
	25%, 75% {opacity: 0;}
}
.flash {
	-webkit-animation-name: flash;
	-moz-animation-name: flash;
	-o-animation-name: flash;
	animation-name: flash;
}
@-webkit-keyframes shake {
	0%, 100% {-webkit-transform: translateX(0);}
	10%, 30%, 50%, 70%, 90% {-webkit-transform: translateX(-10px);}
	20%, 40%, 60%, 80% {-webkit-transform: translateX(10px);}
}
@-moz-keyframes shake {
	0%, 100% {-moz-transform: translateX(0);}
	10%, 30%, 50%, 70%, 90% {-moz-transform: translateX(-10px);}
	20%, 40%, 60%, 80% {-moz-transform: translateX(10px);}
}
@-o-keyframes shake {
	0%, 100% {-o-transform: translateX(0);}
	10%, 30%, 50%, 70%, 90% {-o-transform: translateX(-10px);}
	20%, 40%, 60%, 80% {-o-transform: translateX(10px);}
}
@keyframes shake {
	0%, 100% {transform: translateX(0);}
	10%, 30%, 50%, 70%, 90% {transform: translateX(-10px);}
	20%, 40%, 60%, 80% {transform: translateX(10px);}
}
.shake {
	-webkit-animation-name: shake;
	-moz-animation-name: shake;
	-o-animation-name: shake;
	animation-name: shake;
}
@-webkit-keyframes bounce {
	0%, 20%, 50%, 80%, 100% {-webkit-transform: translateY(0);}
	40% {-webkit-transform: translateY(-30px);}
	60% {-webkit-transform: translateY(-15px);}
}
@-moz-keyframes bounce {
	0%, 20%, 50%, 80%, 100% {-moz-transform: translateY(0);}
	40% {-moz-transform: translateY(-30px);}
	60% {-moz-transform: translateY(-15px);}
}
@-o-keyframes bounce {
	0%, 20%, 50%, 80%, 100% {-o-transform: translateY(0);}
	40% {-o-transform: translateY(-30px);}
	60% {-o-transform: translateY(-15px);}
}
@keyframes bounce {
	0%, 20%, 50%, 80%, 100% {transform: translateY(0);}
	40% {transform: translateY(-30px);}
	60% {transform: translateY(-15px);}
}
.bounce {
	-webkit-animation-name: bounce;
	-moz-animation-name: bounce;
	-o-animation-name: bounce;
	animation-name: bounce;
}
@-webkit-keyframes tada {
	0% {-webkit-transform: scale(1);}	
	10%, 20% {-webkit-transform: scale(0.9) rotate(-3deg);}
	30%, 50%, 70%, 90% {-webkit-transform: scale(1.1) rotate(3deg);}
	40%, 60%, 80% {-webkit-transform: scale(1.1) rotate(-3deg);}
	100% {-webkit-transform: scale(1) rotate(0);}
}
@-moz-keyframes tada {
	0% {-moz-transform: scale(1);}	
	10%, 20% {-moz-transform: scale(0.9) rotate(-3deg);}
	30%, 50%, 70%, 90% {-moz-transform: scale(1.1) rotate(3deg);}
	40%, 60%, 80% {-moz-transform: scale(1.1) rotate(-3deg);}
	100% {-moz-transform: scale(1) rotate(0);}
}
@-o-keyframes tada {
	0% {-o-transform: scale(1);}	
	10%, 20% {-o-transform: scale(0.9) rotate(-3deg);}
	30%, 50%, 70%, 90% {-o-transform: scale(1.1) rotate(3deg);}
	40%, 60%, 80% {-o-transform: scale(1.1) rotate(-3deg);}
	100% {-o-transform: scale(1) rotate(0);}
}
@keyframes tada {
	0% {transform: scale(1);}	
	10%, 20% {transform: scale(0.9) rotate(-3deg);}
	30%, 50%, 70%, 90% {transform: scale(1.1) rotate(3deg);}
	40%, 60%, 80% {transform: scale(1.1) rotate(-3deg);}
	100% {transform: scale(1) rotate(0);}
}
.tada {
	-webkit-animation-name: tada;
	-moz-animation-name: tada;
	-o-animation-name: tada;
	animation-name: tada;
}
@-webkit-keyframes swing {
	20%, 40%, 60%, 80%, 100% { -webkit-transform-origin: top center; }
	20% { -webkit-transform: rotate(15deg); }	
	40% { -webkit-transform: rotate(-10deg); }
	60% { -webkit-transform: rotate(5deg); }	
	80% { -webkit-transform: rotate(-5deg); }	
	100% { -webkit-transform: rotate(0deg); }
}
@-moz-keyframes swing {
	20% { -moz-transform: rotate(15deg); }	
	40% { -moz-transform: rotate(-10deg); }
	60% { -moz-transform: rotate(5deg); }	
	80% { -moz-transform: rotate(-5deg); }	
	100% { -moz-transform: rotate(0deg); }
}
@-o-keyframes swing {
	20% { -o-transform: rotate(15deg); }	
	40% { -o-transform: rotate(-10deg); }
	60% { -o-transform: rotate(5deg); }	
	80% { -o-transform: rotate(-5deg); }	
	100% { -o-transform: rotate(0deg); }
}
@keyframes swing {
	20% { transform: rotate(15deg); }	
	40% { transform: rotate(-10deg); }
	60% { transform: rotate(5deg); }	
	80% { transform: rotate(-5deg); }	
	100% { transform: rotate(0deg); }
}
.swing {
	-webkit-transform-origin: top center;
	-moz-transform-origin: top center;
	-o-transform-origin: top center;
	transform-origin: top center;
	-webkit-animation-name: swing;
	-moz-animation-name: swing;
	-o-animation-name: swing;
	animation-name: swing;
}
/* originally authored by Nick Pettit - https://github.com/nickpettit/glide */
@-webkit-keyframes wobble {
  0% { -webkit-transform: translateX(0%); }
  15% { -webkit-transform: translateX(-25%) rotate(-5deg); }
  30% { -webkit-transform: translateX(20%) rotate(3deg); }
  45% { -webkit-transform: translateX(-15%) rotate(-3deg); }
  60% { -webkit-transform: translateX(10%) rotate(2deg); }
  75% { -webkit-transform: translateX(-5%) rotate(-1deg); }
  100% { -webkit-transform: translateX(0%); }
}
@-moz-keyframes wobble {
  0% { -moz-transform: translateX(0%); }
  15% { -moz-transform: translateX(-25%) rotate(-5deg); }
  30% { -moz-transform: translateX(20%) rotate(3deg); }
  45% { -moz-transform: translateX(-15%) rotate(-3deg); }
  60% { -moz-transform: translateX(10%) rotate(2deg); }
  75% { -moz-transform: translateX(-5%) rotate(-1deg); }
  100% { -moz-transform: translateX(0%); }
}
@-o-keyframes wobble {
  0% { -o-transform: translateX(0%); }
  15% { -o-transform: translateX(-25%) rotate(-5deg); }
  30% { -o-transform: translateX(20%) rotate(3deg); }
  45% { -o-transform: translateX(-15%) rotate(-3deg); }
  60% { -o-transform: translateX(10%) rotate(2deg); }
  75% { -o-transform: translateX(-5%) rotate(-1deg); }
  100% { -o-transform: translateX(0%); }
}
@keyframes wobble {
  0% { transform: translateX(0%); }
  15% { transform: translateX(-25%) rotate(-5deg); }
  30% { transform: translateX(20%) rotate(3deg); }
  45% { transform: translateX(-15%) rotate(-3deg); }
  60% { transform: translateX(10%) rotate(2deg); }
  75% { transform: translateX(-5%) rotate(-1deg); }
  100% { transform: translateX(0%); }
}
.wobble {
	-webkit-animation-name: wobble;
	-moz-animation-name: wobble;
	-o-animation-name: wobble;
	animation-name: wobble;
}
/* originally authored by Nick Pettit - https://github.com/nickpettit/glide */
@-webkit-keyframes pulse {
    0% { -webkit-transform: scale(1); }	
	50% { -webkit-transform: scale(1.1); }
    100% { -webkit-transform: scale(1); }
}
@-moz-keyframes pulse {
    0% { -moz-transform: scale(1); }	
	50% { -moz-transform: scale(1.1); }
    100% { -moz-transform: scale(1); }
}
@-o-keyframes pulse {
    0% { -o-transform: scale(1); }	
	50% { -o-transform: scale(1.1); }
    100% { -o-transform: scale(1); }
}
@keyframes pulse {
    0% { transform: scale(1); }	
	50% { transform: scale(1.1); }
    100% { transform: scale(1); }
}
.pulse {
	-webkit-animation-name: pulse;
	-moz-animation-name: pulse;
	-o-animation-name: pulse;
	animation-name: pulse;
}
@-webkit-keyframes flip {
	0% {
		-webkit-transform: perspective(400px) translateZ(0) rotateY(0) scale(1);
		-webkit-animation-timing-function: ease-out;
	}
	40% {
		-webkit-transform: perspective(400px) translateZ(150px) rotateY(170deg) scale(1);
		-webkit-animation-timing-function: ease-out;
	}
	50% {
		-webkit-transform: perspective(400px) translateZ(150px) rotateY(190deg) scale(1);
		-webkit-animation-timing-function: ease-in;
	}
	80% {
		-webkit-transform: perspective(400px) translateZ(0) rotateY(360deg) scale(.95);
		-webkit-animation-timing-function: ease-in;
	}
	100% {
		-webkit-transform: perspective(400px) translateZ(0) rotateY(360deg) scale(1);
		-webkit-animation-timing-function: ease-in;
	}
}
@-moz-keyframes flip {
	0% {
		-moz-transform: perspective(400px) translateZ(0) rotateY(0) scale(1);
		-moz-animation-timing-function: ease-out;
	}
	40% {
		-moz-transform: perspective(400px) translateZ(150px) rotateY(170deg) scale(1);
		-moz-animation-timing-function: ease-out;
	}
	50% {
		-moz-transform: perspective(400px) translateZ(150px) rotateY(190deg) scale(1);
		-moz-animation-timing-function: ease-in;
	}
	80% {
		-moz-transform: perspective(400px) translateZ(0) rotateY(360deg) scale(.95);
		-moz-animation-timing-function: ease-in;
	}
	100% {
		-moz-transform: perspective(400px) translateZ(0) rotateY(360deg) scale(1);
		-moz-animation-timing-function: ease-in;
	}
}
@-o-keyframes flip {
	0% {
		-o-transform: perspective(400px) translateZ(0) rotateY(0) scale(1);
		-o-animation-timing-function: ease-out;
	}
	40% {
		-o-transform: perspective(400px) translateZ(150px) rotateY(170deg) scale(1);
		-o-animation-timing-function: ease-out;
	}
	50% {
		-o-transform: perspective(400px) translateZ(150px) rotateY(190deg) scale(1);
		-o-animation-timing-function: ease-in;
	}
	80% {
		-o-transform: perspective(400px) translateZ(0) rotateY(360deg) scale(.95);
		-o-animation-timing-function: ease-in;
	}
	100% {
		-o-transform: perspective(400px) translateZ(0) rotateY(360deg) scale(1);
		-o-animation-timing-function: ease-in;
	}
}
@keyframes flip {
	0% {
		transform: perspective(400px) translateZ(0) rotateY(0) scale(1);
		animation-timing-function: ease-out;
	}
	40% {
		transform: perspective(400px) translateZ(150px) rotateY(170deg) scale(1);
		animation-timing-function: ease-out;
	}
	50% {
		transform: perspective(400px) translateZ(150px) rotateY(190deg) scale(1);
		animation-timing-function: ease-in;
	}
	80% {
		transform: perspective(400px) translateZ(0) rotateY(360deg) scale(.95);
		animation-timing-function: ease-in;
	}
	100% {
		transform: perspective(400px) translateZ(0) rotateY(360deg) scale(1);
		animation-timing-function: ease-in;
	}
}
.animated.flip {
	-webkit-backface-visibility: visible !important;
	-webkit-animation-name: flip;
	-moz-backface-visibility: visible !important;
	-moz-animation-name: flip;
	-o-backface-visibility: visible !important;
	-o-animation-name: flip;
	backface-visibility: visible !important;
	animation-name: flip;
}
@-webkit-keyframes flipInX {
    0% {
        -webkit-transform: perspective(400px) rotateX(90deg);
        opacity: 0;
    }
    40% {
        -webkit-transform: perspective(400px) rotateX(-10deg);
    }
    70% {
        -webkit-transform: perspective(400px) rotateX(10deg);
    }
    100% {
        -webkit-transform: perspective(400px) rotateX(0deg);
        opacity: 1;
    }
}
@-moz-keyframes flipInX {
    0% {
        -moz-transform: perspective(400px) rotateX(90deg);
        opacity: 0;
    }
    40% {
        -moz-transform: perspective(400px) rotateX(-10deg);
    }
    70% {
        -moz-transform: perspective(400px) rotateX(10deg);
    }
    100% {
        -moz-transform: perspective(400px) rotateX(0deg);
        opacity: 1;
    }
}
@-o-keyframes flipInX {
    0% {
        -o-transform: perspective(400px) rotateX(90deg);
        opacity: 0;
    }
    40% {
        -o-transform: perspective(400px) rotateX(-10deg);
    }
    70% {
        -o-transform: perspective(400px) rotateX(10deg);
    }
    100% {
        -o-transform: perspective(400px) rotateX(0deg);
        opacity: 1;
    }
}
@keyframes flipInX {
    0% {
        transform: perspective(400px) rotateX(90deg);
        opacity: 0;
    }
    40% {
        transform: perspective(400px) rotateX(-10deg);
    }
    70% {
        transform: perspective(400px) rotateX(10deg);
    }
    100% {
        transform: perspective(400px) rotateX(0deg);
        opacity: 1;
    }
}
.flipInX {
	-webkit-backface-visibility: visible !important;
	-webkit-animation-name: flipInX;
	-moz-backface-visibility: visible !important;
	-moz-animation-name: flipInX;
	-o-backface-visibility: visible !important;
	-o-animation-name: flipInX;
	backface-visibility: visible !important;
	animation-name: flipInX;
}
@-webkit-keyframes flipOutX {
    0% {
        -webkit-transform: perspective(400px) rotateX(0deg);
        opacity: 1;
    }
	100% {
        -webkit-transform: perspective(400px) rotateX(90deg);
        opacity: 0;
    }
}
@-moz-keyframes flipOutX {
    0% {
        -moz-transform: perspective(400px) rotateX(0deg);
        opacity: 1;
    }
	100% {
        -moz-transform: perspective(400px) rotateX(90deg);
        opacity: 0;
    }
}
@-o-keyframes flipOutX {
    0% {
        -o-transform: perspective(400px) rotateX(0deg);
        opacity: 1;
    }
	100% {
        -o-transform: perspective(400px) rotateX(90deg);
        opacity: 0;
    }
}
@keyframes flipOutX {
    0% {
        transform: perspective(400px) rotateX(0deg);
        opacity: 1;
    }
	100% {
        transform: perspective(400px) rotateX(90deg);
        opacity: 0;
    }
}
.flipOutX {
	-webkit-animation-name: flipOutX;
	-webkit-backface-visibility: visible !important;
	-moz-animation-name: flipOutX;
	-moz-backface-visibility: visible !important;
	-o-animation-name: flipOutX;
	-o-backface-visibility: visible !important;
	animation-name: flipOutX;
	backface-visibility: visible !important;
}
@-webkit-keyframes flipInY {
    0% {
        -webkit-transform: perspective(400px) rotateY(90deg);
        opacity: 0;
    }
    40% {
        -webkit-transform: perspective(400px) rotateY(-10deg);
    }
    70% {
        -webkit-transform: perspective(400px) rotateY(10deg);
    }
    100% {
        -webkit-transform: perspective(400px) rotateY(0deg);
        opacity: 1;
    }
}
@-moz-keyframes flipInY {
    0% {
        -moz-transform: perspective(400px) rotateY(90deg);
        opacity: 0;
    }
    40% {
        -moz-transform: perspective(400px) rotateY(-10deg);
    }
    70% {
        -moz-transform: perspective(400px) rotateY(10deg);
    }
    100% {
        -moz-transform: perspective(400px) rotateY(0deg);
        opacity: 1;
    }
}
@-o-keyframes flipInY {
    0% {
        -o-transform: perspective(400px) rotateY(90deg);
        opacity: 0;
    }
    40% {
        -o-transform: perspective(400px) rotateY(-10deg);
    }
    70% {
        -o-transform: perspective(400px) rotateY(10deg);
    }
    100% {
        -o-transform: perspective(400px) rotateY(0deg);
        opacity: 1;
    }
}
@keyframes flipInY {
    0% {
        transform: perspective(400px) rotateY(90deg);
        opacity: 0;
    }
    40% {
        transform: perspective(400px) rotateY(-10deg);
    }
    70% {
        transform: perspective(400px) rotateY(10deg);
    }
    100% {
        transform: perspective(400px) rotateY(0deg);
        opacity: 1;
    }
}
.flipInY {
	-webkit-backface-visibility: visible !important;
	-webkit-animation-name: flipInY;
	-moz-backface-visibility: visible !important;
	-moz-animation-name: flipInY;
	-o-backface-visibility: visible !important;
	-o-animation-name: flipInY;
	backface-visibility: visible !important;
	animation-name: flipInY;
}
@-webkit-keyframes flipOutY {
    0% {
        -webkit-transform: perspective(400px) rotateY(0deg);
        opacity: 1;
    }
	100% {
        -webkit-transform: perspective(400px) rotateY(90deg);
        opacity: 0;
    }
}
@-moz-keyframes flipOutY {
    0% {
        -moz-transform: perspective(400px) rotateY(0deg);
        opacity: 1;
    }
	100% {
        -moz-transform: perspective(400px) rotateY(90deg);
        opacity: 0;
    }
}
@-o-keyframes flipOutY {
    0% {
        -o-transform: perspective(400px) rotateY(0deg);
        opacity: 1;
    }
	100% {
        -o-transform: perspective(400px) rotateY(90deg);
        opacity: 0;
    }
}
@keyframes flipOutY {
    0% {
        transform: perspective(400px) rotateY(0deg);
        opacity: 1;
    }
	100% {
        transform: perspective(400px) rotateY(90deg);
        opacity: 0;
    }
}
.flipOutY {
	-webkit-backface-visibility: visible !important;
	-webkit-animation-name: flipOutY;
	-moz-backface-visibility: visible !important;
	-moz-animation-name: flipOutY;
	-o-backface-visibility: visible !important;
	-o-animation-name: flipOutY;
	backface-visibility: visible !important;
	animation-name: flipOutY;
}
@-webkit-keyframes fadeIn {
	0% {opacity: 0;}	
	100% {opacity: 1;}
}
@-moz-keyframes fadeIn {
	0% {opacity: 0;}	
	100% {opacity: 1;}
}
@-o-keyframes fadeIn {
	0% {opacity: 0;}	
	100% {opacity: 1;}
}
@keyframes fadeIn {
	0% {opacity: 0;}	
	100% {opacity: 1;}
}
.fadeIn {
	-webkit-animation-name: fadeIn;
	-moz-animation-name: fadeIn;
	-o-animation-name: fadeIn;
	animation-name: fadeIn;
}
@-webkit-keyframes fadeInUp {
	0% {
		opacity: 0;
		-webkit-transform: translateY(20px);
	}
	100% {
		opacity: 1;
		-webkit-transform: translateY(0);
	}
}
@-moz-keyframes fadeInUp {
	0% {
		opacity: 0;
		-moz-transform: translateY(20px);
	}
	100% {
		opacity: 1;
		-moz-transform: translateY(0);
	}
}
@-o-keyframes fadeInUp {
	0% {
		opacity: 0;
		-o-transform: translateY(20px);
	}
	100% {
		opacity: 1;
		-o-transform: translateY(0);
	}
}
@keyframes fadeInUp {
	0% {
		opacity: 0;
		transform: translateY(20px);
	}
	100% {
		opacity: 1;
		transform: translateY(0);
	}
}
.fadeInUp {
	-webkit-animation-name: fadeInUp;
	-moz-animation-name: fadeInUp;
	-o-animation-name: fadeInUp;
	animation-name: fadeInUp;
}
@-webkit-keyframes fadeInDown {
	0% {
		opacity: 0;
		-webkit-transform: translateY(-20px);
	}
	100% {
		opacity: 1;
		-webkit-transform: translateY(0);
	}
}
@-moz-keyframes fadeInDown {
	0% {
		opacity: 0;
		-moz-transform: translateY(-20px);
	}
	100% {
		opacity: 1;
		-moz-transform: translateY(0);
	}
}
@-o-keyframes fadeInDown {
	0% {
		opacity: 0;
		-o-transform: translateY(-20px);
	}
	100% {
		opacity: 1;
		-o-transform: translateY(0);
	}
}
@keyframes fadeInDown {
	0% {
		opacity: 0;
		transform: translateY(-20px);
	}
	100% {
		opacity: 1;
		transform: translateY(0);
	}
}
.fadeInDown {
	-webkit-animation-name: fadeInDown;
	-moz-animation-name: fadeInDown;
	-o-animation-name: fadeInDown;
	animation-name: fadeInDown;
}
@-webkit-keyframes fadeInLeft {
	0% {
		opacity: 0;
		-webkit-transform: translateX(-20px);
	}
	100% {
		opacity: 1;
		-webkit-transform: translateX(0);
	}
}
@-moz-keyframes fadeInLeft {
	0% {
		opacity: 0;
		-moz-transform: translateX(-20px);
	}
	100% {
		opacity: 1;
		-moz-transform: translateX(0);
	}
}
@-o-keyframes fadeInLeft {
	0% {
		opacity: 0;
		-o-transform: translateX(-20px);
	}
	100% {
		opacity: 1;
		-o-transform: translateX(0);
	}
}
@keyframes fadeInLeft {
	0% {
		opacity: 0;
		transform: translateX(-20px);
	}
	100% {
		opacity: 1;
		transform: translateX(0);
	}
}
.fadeInLeft {
	-webkit-animation-name: fadeInLeft;
	-moz-animation-name: fadeInLeft;
	-o-animation-name: fadeInLeft;
	animation-name: fadeInLeft;
}
@-webkit-keyframes fadeInRight {
	0% {
		opacity: 0;
		-webkit-transform: translateX(20px);
	}
	100% {
		opacity: 1;
		-webkit-transform: translateX(0);
	}
}
@-moz-keyframes fadeInRight {
	0% {
		opacity: 0;
		-moz-transform: translateX(20px);
	}
	100% {
		opacity: 1;
		-moz-transform: translateX(0);
	}
}
@-o-keyframes fadeInRight {
	0% {
		opacity: 0;
		-o-transform: translateX(20px);
	}
	100% {
		opacity: 1;
		-o-transform: translateX(0);
	}
}
@keyframes fadeInRight {
	0% {
		opacity: 0;
		transform: translateX(20px);
	}
	100% {
		opacity: 1;
		transform: translateX(0);
	}
}
.fadeInRight {
	-webkit-animation-name: fadeInRight;
	-moz-animation-name: fadeInRight;
	-o-animation-name: fadeInRight;
	animation-name: fadeInRight;
}
@-webkit-keyframes fadeInUpBig {
	0% {
		opacity: 0;
		-webkit-transform: translateY(2000px);
	}
	100% {
		opacity: 1;
		-webkit-transform: translateY(0);
	}
}
@-moz-keyframes fadeInUpBig {
	0% {
		opacity: 0;
		-moz-transform: translateY(2000px);
	}
	100% {
		opacity: 1;
		-moz-transform: translateY(0);
	}
}
@-o-keyframes fadeInUpBig {
	0% {
		opacity: 0;
		-o-transform: translateY(2000px);
	}
	100% {
		opacity: 1;
		-o-transform: translateY(0);
	}
}
@keyframes fadeInUpBig {
	0% {
		opacity: 0;
		transform: translateY(2000px);
	}
	100% {
		opacity: 1;
		transform: translateY(0);
	}
}
.fadeInUpBig {
	-webkit-animation-name: fadeInUpBig;
	-moz-animation-name: fadeInUpBig;
	-o-animation-name: fadeInUpBig;
	animation-name: fadeInUpBig;
}
@-webkit-keyframes fadeInDownBig {
	0% {
		opacity: 0;
		-webkit-transform: translateY(-2000px);
	}
	100% {
		opacity: 1;
		-webkit-transform: translateY(0);
	}
}
@-moz-keyframes fadeInDownBig {
	0% {
		opacity: 0;
		-moz-transform: translateY(-2000px);
	}
	100% {
		opacity: 1;
		-moz-transform: translateY(0);
	}
}
@-o-keyframes fadeInDownBig {
	0% {
		opacity: 0;
		-o-transform: translateY(-2000px);
	}
	100% {
		opacity: 1;
		-o-transform: translateY(0);
	}
}
@keyframes fadeInDownBig {
	0% {
		opacity: 0;
		transform: translateY(-2000px);
	}
	100% {
		opacity: 1;
		transform: translateY(0);
	}
}
.fadeInDownBig {
	-webkit-animation-name: fadeInDownBig;
	-moz-animation-name: fadeInDownBig;
	-o-animation-name: fadeInDownBig;
	animation-name: fadeInDownBig;
}
@-webkit-keyframes fadeInLeftBig {
	0% {
		opacity: 0;
		-webkit-transform: translateX(-2000px);
	}
	100% {
		opacity: 1;
		-webkit-transform: translateX(0);
	}
}
@-moz-keyframes fadeInLeftBig {
	0% {
		opacity: 0;
		-moz-transform: translateX(-2000px);
	}
	100% {
		opacity: 1;
		-moz-transform: translateX(0);
	}
}
@-o-keyframes fadeInLeftBig {
	0% {
		opacity: 0;
		-o-transform: translateX(-2000px);
	}
	100% {
		opacity: 1;
		-o-transform: translateX(0);
	}
}
@keyframes fadeInLeftBig {
	0% {
		opacity: 0;
		transform: translateX(-2000px);
	}
	100% {
		opacity: 1;
		transform: translateX(0);
	}
}
.fadeInLeftBig {
	-webkit-animation-name: fadeInLeftBig;
	-moz-animation-name: fadeInLeftBig;
	-o-animation-name: fadeInLeftBig;
	animation-name: fadeInLeftBig;
}
@-webkit-keyframes fadeInRightBig {
	0% {
		opacity: 0;
		-webkit-transform: translateX(2000px);
	}
	100% {
		opacity: 1;
		-webkit-transform: translateX(0);
	}
}
@-moz-keyframes fadeInRightBig {
	0% {
		opacity: 0;
		-moz-transform: translateX(2000px);
	}
	100% {
		opacity: 1;
		-moz-transform: translateX(0);
	}
}
@-o-keyframes fadeInRightBig {
	0% {
		opacity: 0;
		-o-transform: translateX(2000px);
	}
	100% {
		opacity: 1;
		-o-transform: translateX(0);
	}
}
@keyframes fadeInRightBig {
	0% {
		opacity: 0;
		transform: translateX(2000px);
	}
	100% {
		opacity: 1;
		transform: translateX(0);
	}
}
.fadeInRightBig {
	-webkit-animation-name: fadeInRightBig;
	-moz-animation-name: fadeInRightBig;
	-o-animation-name: fadeInRightBig;
	animation-name: fadeInRightBig;
}
@-webkit-keyframes fadeOut {
	0% {opacity: 1;}
	100% {opacity: 0;}
}
@-moz-keyframes fadeOut {
	0% {opacity: 1;}
	100% {opacity: 0;}
}
@-o-keyframes fadeOut {
	0% {opacity: 1;}
	100% {opacity: 0;}
}
@keyframes fadeOut {
	0% {opacity: 1;}
	100% {opacity: 0;}
}
.fadeOut {
	-webkit-animation-name: fadeOut;
	-moz-animation-name: fadeOut;
	-o-animation-name: fadeOut;
	animation-name: fadeOut;
}
@-webkit-keyframes fadeOutUp {
	0% {
		opacity: 1;
		-webkit-transform: translateY(0);
	}
	100% {
		opacity: 0;
		-webkit-transform: translateY(-20px);
	}
}
@-moz-keyframes fadeOutUp {
	0% {
		opacity: 1;
		-moz-transform: translateY(0);
	}
	100% {
		opacity: 0;
		-moz-transform: translateY(-20px);
	}
}
@-o-keyframes fadeOutUp {
	0% {
		opacity: 1;
		-o-transform: translateY(0);
	}
	100% {
		opacity: 0;
		-o-transform: translateY(-20px);
	}
}
@keyframes fadeOutUp {
	0% {
		opacity: 1;
		transform: translateY(0);
	}
	100% {
		opacity: 0;
		transform: translateY(-20px);
	}
}
.fadeOutUp {
	-webkit-animation-name: fadeOutUp;
	-moz-animation-name: fadeOutUp;
	-o-animation-name: fadeOutUp;
	animation-name: fadeOutUp;
}
@-webkit-keyframes fadeOutDown {
	0% {
		opacity: 1;
		-webkit-transform: translateY(0);
	}
	100% {
		opacity: 0;
		-webkit-transform: translateY(20px);
	}
}
@-moz-keyframes fadeOutDown {
	0% {
		opacity: 1;
		-moz-transform: translateY(0);
	}
	100% {
		opacity: 0;
		-moz-transform: translateY(20px);
	}
}
@-o-keyframes fadeOutDown {
	0% {
		opacity: 1;
		-o-transform: translateY(0);
	}
	100% {
		opacity: 0;
		-o-transform: translateY(20px);
	}
}
@keyframes fadeOutDown {
	0% {
		opacity: 1;
		transform: translateY(0);
	}
	100% {
		opacity: 0;
		transform: translateY(20px);
	}
}
.fadeOutDown {
	-webkit-animation-name: fadeOutDown;
	-moz-animation-name: fadeOutDown;
	-o-animation-name: fadeOutDown;
	animation-name: fadeOutDown;
}
@-webkit-keyframes fadeOutLeft {
	0% {
		opacity: 1;
		-webkit-transform: translateX(0);
	}
	100% {
		opacity: 0;
		-webkit-transform: translateX(-20px);
	}
}
@-moz-keyframes fadeOutLeft {
	0% {
		opacity: 1;
		-moz-transform: translateX(0);
	}
	100% {
		opacity: 0;
		-moz-transform: translateX(-20px);
	}
}
@-o-keyframes fadeOutLeft {
	0% {
		opacity: 1;
		-o-transform: translateX(0);
	}
	100% {
		opacity: 0;
		-o-transform: translateX(-20px);
	}
}
@keyframes fadeOutLeft {
	0% {
		opacity: 1;
		transform: translateX(0);
	}
	100% {
		opacity: 0;
		transform: translateX(-20px);
	}
}
.fadeOutLeft {
	-webkit-animation-name: fadeOutLeft;
	-moz-animation-name: fadeOutLeft;
	-o-animation-name: fadeOutLeft;
	animation-name: fadeOutLeft;
}
@-webkit-keyframes fadeOutRight {
	0% {
		opacity: 1;
		-webkit-transform: translateX(0);
	}
	100% {
		opacity: 0;
		-webkit-transform: translateX(20px);
	}
}
@-moz-keyframes fadeOutRight {
	0% {
		opacity: 1;
		-moz-transform: translateX(0);
	}
	100% {
		opacity: 0;
		-moz-transform: translateX(20px);
	}
}
@-o-keyframes fadeOutRight {
	0% {
		opacity: 1;
		-o-transform: translateX(0);
	}
	100% {
		opacity: 0;
		-o-transform: translateX(20px);
	}
}
@keyframes fadeOutRight {
	0% {
		opacity: 1;
		transform: translateX(0);
	}
	100% {
		opacity: 0;
		transform: translateX(20px);
	}
}
.fadeOutRight {
	-webkit-animation-name: fadeOutRight;
	-moz-animation-name: fadeOutRight;
	-o-animation-name: fadeOutRight;
	animation-name: fadeOutRight;
}
@-webkit-keyframes fadeOutUpBig {
	0% {
		opacity: 1;
		-webkit-transform: translateY(0);
	}
	100% {
		opacity: 0;
		-webkit-transform: translateY(-2000px);
	}
}
@-moz-keyframes fadeOutUpBig {
	0% {
		opacity: 1;
		-moz-transform: translateY(0);
	}
	100% {
		opacity: 0;
		-moz-transform: translateY(-2000px);
	}
}
@-o-keyframes fadeOutUpBig {
	0% {
		opacity: 1;
		-o-transform: translateY(0);
	}
	100% {
		opacity: 0;
		-o-transform: translateY(-2000px);
	}
}
@keyframes fadeOutUpBig {
	0% {
		opacity: 1;
		transform: translateY(0);
	}
	100% {
		opacity: 0;
		transform: translateY(-2000px);
	}
}
.fadeOutUpBig {
	-webkit-animation-name: fadeOutUpBig;
	-moz-animation-name: fadeOutUpBig;
	-o-animation-name: fadeOutUpBig;
	animation-name: fadeOutUpBig;
}
@-webkit-keyframes fadeOutDownBig {
	0% {
		opacity: 1;
		-webkit-transform: translateY(0);
	}
	100% {
		opacity: 0;
		-webkit-transform: translateY(2000px);
	}
}
@-moz-keyframes fadeOutDownBig {
	0% {
		opacity: 1;
		-moz-transform: translateY(0);
	}
	100% {
		opacity: 0;
		-moz-transform: translateY(2000px);
	}
}
@-o-keyframes fadeOutDownBig {
	0% {
		opacity: 1;
		-o-transform: translateY(0);
	}
	100% {
		opacity: 0;
		-o-transform: translateY(2000px);
	}
}
@keyframes fadeOutDownBig {
	0% {
		opacity: 1;
		transform: translateY(0);
	}
	100% {
		opacity: 0;
		transform: translateY(2000px);
	}
}
.fadeOutDownBig {
	-webkit-animation-name: fadeOutDownBig;
	-moz-animation-name: fadeOutDownBig;
	-o-animation-name: fadeOutDownBig;
	animation-name: fadeOutDownBig;
}
@-webkit-keyframes fadeOutLeftBig {
	0% {
		opacity: 1;
		-webkit-transform: translateX(0);
	}
	100% {
		opacity: 0;
		-webkit-transform: translateX(-2000px);
	}
}
@-moz-keyframes fadeOutLeftBig {
	0% {
		opacity: 1;
		-moz-transform: translateX(0);
	}
	100% {
		opacity: 0;
		-moz-transform: translateX(-2000px);
	}
}
@-o-keyframes fadeOutLeftBig {
	0% {
		opacity: 1;
		-o-transform: translateX(0);
	}
	100% {
		opacity: 0;
		-o-transform: translateX(-2000px);
	}
}
@keyframes fadeOutLeftBig {
	0% {
		opacity: 1;
		transform: translateX(0);
	}
	100% {
		opacity: 0;
		transform: translateX(-2000px);
	}
}
.fadeOutLeftBig {
	-webkit-animation-name: fadeOutLeftBig;
	-moz-animation-name: fadeOutLeftBig;
	-o-animation-name: fadeOutLeftBig;
	animation-name: fadeOutLeftBig;
}
@-webkit-keyframes fadeOutRightBig {
	0% {
		opacity: 1;
		-webkit-transform: translateX(0);
	}
	100% {
		opacity: 0;
		-webkit-transform: translateX(2000px);
	}
}
@-moz-keyframes fadeOutRightBig {
	0% {
		opacity: 1;
		-moz-transform: translateX(0);
	}
	100% {
		opacity: 0;
		-moz-transform: translateX(2000px);
	}
}
@-o-keyframes fadeOutRightBig {
	0% {
		opacity: 1;
		-o-transform: translateX(0);
	}
	100% {
		opacity: 0;
		-o-transform: translateX(2000px);
	}
}
@keyframes fadeOutRightBig {
	0% {
		opacity: 1;
		transform: translateX(0);
	}
	100% {
		opacity: 0;
		transform: translateX(2000px);
	}
}
.fadeOutRightBig {
	-webkit-animation-name: fadeOutRightBig;
	-moz-animation-name: fadeOutRightBig;
	-o-animation-name: fadeOutRightBig;
	animation-name: fadeOutRightBig;
}
@-webkit-keyframes slideInDown {
	0% {
		opacity: 0;
		-webkit-transform: translateY(-2000px);
	}
	100% {
		-webkit-transform: translateY(0);
	}
}
@-moz-keyframes slideInDown {
	0% {
		opacity: 0;
		-moz-transform: translateY(-2000px);
	}
	100% {
		-moz-transform: translateY(0);
	}
}
@-o-keyframes slideInDown {
	0% {
		opacity: 0;
		-o-transform: translateY(-2000px);
	}
	100% {
		-o-transform: translateY(0);
	}
}
@keyframes slideInDown {
	0% {
		opacity: 0;
		transform: translateY(-2000px);
	}
	100% {
		transform: translateY(0);
	}
}
.slideInDown {
	-webkit-animation-name: slideInDown;
	-moz-animation-name: slideInDown;
	-o-animation-name: slideInDown;
	animation-name: slideInDown;
}
@-webkit-keyframes slideInLeft {
	0% {
		opacity: 0;
		-webkit-transform: translateX(-2000px);
	}
	100% {
		-webkit-transform: translateX(0);
	}
}
@-moz-keyframes slideInLeft {
	0% {
		opacity: 0;
		-moz-transform: translateX(-2000px);
	}
	100% {
		-moz-transform: translateX(0);
	}
}
@-o-keyframes slideInLeft {
	0% {
		opacity: 0;
		-o-transform: translateX(-2000px);
	}
	100% {
		-o-transform: translateX(0);
	}
}
@keyframes slideInLeft {
	0% {
		opacity: 0;
		transform: translateX(-2000px);
	}
	100% {
		transform: translateX(0);
	}
}
.slideInLeft {
	-webkit-animation-name: slideInLeft;
	-moz-animation-name: slideInLeft;
	-o-animation-name: slideInLeft;
	animation-name: slideInLeft;
}
@-webkit-keyframes slideInRight {
	0% {
		opacity: 0;
		-webkit-transform: translateX(2000px);
	}
	100% {
		-webkit-transform: translateX(0);
	}
}
@-moz-keyframes slideInRight {
	0% {
		opacity: 0;
		-moz-transform: translateX(2000px);
	}
	100% {
		-moz-transform: translateX(0);
	}
}
@-o-keyframes slideInRight {
	0% {
		opacity: 0;
		-o-transform: translateX(2000px);
	}
	100% {
		-o-transform: translateX(0);
	}
}
@keyframes slideInRight {
	0% {
		opacity: 0;
		transform: translateX(2000px);
	}
	100% {
		transform: translateX(0);
	}
}
.slideInRight {
	-webkit-animation-name: slideInRight;
	-moz-animation-name: slideInRight;
	-o-animation-name: slideInRight;
	animation-name: slideInRight;
}
@-webkit-keyframes slideOutUp {
	0% {
		-webkit-transform: translateY(0);
	}
	100% {
		opacity: 0;
		-webkit-transform: translateY(-2000px);
	}
}
@-moz-keyframes slideOutUp {
	0% {
		-moz-transform: translateY(0);
	}
	100% {
		opacity: 0;
		-moz-transform: translateY(-2000px);
	}
}
@-o-keyframes slideOutUp {
	0% {
		-o-transform: translateY(0);
	}
	100% {
		opacity: 0;
		-o-transform: translateY(-2000px);
	}
}
@keyframes slideOutUp {
	0% {
		transform: translateY(0);
	}
	100% {
		opacity: 0;
		transform: translateY(-2000px);
	}
}
.slideOutUp {
	-webkit-animation-name: slideOutUp;
	-moz-animation-name: slideOutUp;
	-o-animation-name: slideOutUp;
	animation-name: slideOutUp;
}
@-webkit-keyframes slideOutLeft {
	0% {
		-webkit-transform: translateX(0);
	}
	100% {
		opacity: 0;
		-webkit-transform: translateX(-2000px);
	}
}
@-moz-keyframes slideOutLeft {
	0% {
		-moz-transform: translateX(0);
	}
	100% {
		opacity: 0;
		-moz-transform: translateX(-2000px);
	}
}
@-o-keyframes slideOutLeft {
	0% {
		-o-transform: translateX(0);
	}
	100% {
		opacity: 0;
		-o-transform: translateX(-2000px);
	}
}
@keyframes slideOutLeft {
	0% {
		transform: translateX(0);
	}
	100% {
		opacity: 0;
		transform: translateX(-2000px);
	}
}
.slideOutLeft {
	-webkit-animation-name: slideOutLeft;
	-moz-animation-name: slideOutLeft;
	-o-animation-name: slideOutLeft;
	animation-name: slideOutLeft;
}
@-webkit-keyframes slideOutRight {
	0% {
		-webkit-transform: translateX(0);
	}
	100% {
		opacity: 0;
		-webkit-transform: translateX(2000px);
	}
}
@-moz-keyframes slideOutRight {
	0% {
		-moz-transform: translateX(0);
	}
	100% {
		opacity: 0;
		-moz-transform: translateX(2000px);
	}
}
@-o-keyframes slideOutRight {
	0% {
		-o-transform: translateX(0);
	}
	100% {
		opacity: 0;
		-o-transform: translateX(2000px);
	}
}
@keyframes slideOutRight {
	0% {
		transform: translateX(0);
	}
	100% {
		opacity: 0;
		transform: translateX(2000px);
	}
}
.slideOutRight {
	-webkit-animation-name: slideOutRight;
	-moz-animation-name: slideOutRight;
	-o-animation-name: slideOutRight;
	animation-name: slideOutRight;
}
@-webkit-keyframes bounceIn {
	0% {
		opacity: 0;
		-webkit-transform: scale(.3);
	}
	50% {
		opacity: 1;
		-webkit-transform: scale(1.05);
	}
	70% {
		-webkit-transform: scale(.9);
	}
	100% {
		-webkit-transform: scale(1);
	}
}
@-moz-keyframes bounceIn {
	0% {
		opacity: 0;
		-moz-transform: scale(.3);
	}
	50% {
		opacity: 1;
		-moz-transform: scale(1.05);
	}
	70% {
		-moz-transform: scale(.9);
	}
	100% {
		-moz-transform: scale(1);
	}
}
@-o-keyframes bounceIn {
	0% {
		opacity: 0;
		-o-transform: scale(.3);
	}
	50% {
		opacity: 1;
		-o-transform: scale(1.05);
	}
	70% {
		-o-transform: scale(.9);
	}
	100% {
		-o-transform: scale(1);
	}
}
@keyframes bounceIn {
	0% {
		opacity: 0;
		transform: scale(.3);
	}
	50% {
		opacity: 1;
		transform: scale(1.05);
	}
	70% {
		transform: scale(.9);
	}
	100% {
		transform: scale(1);
	}
}
.bounceIn {
	-webkit-animation-name: bounceIn;
	-moz-animation-name: bounceIn;
	-o-animation-name: bounceIn;
	animation-name: bounceIn;
}
@-webkit-keyframes bounceInUp {
	0% {
		opacity: 0;
		-webkit-transform: translateY(2000px);
	}
	60% {
		opacity: 1;
		-webkit-transform: translateY(-30px);
	}
	80% {
		-webkit-transform: translateY(10px);
	}
	100% {
		-webkit-transform: translateY(0);
	}
}
@-moz-keyframes bounceInUp {
	0% {
		opacity: 0;
		-moz-transform: translateY(2000px);
	}
	60% {
		opacity: 1;
		-moz-transform: translateY(-30px);
	}
	80% {
		-moz-transform: translateY(10px);
	}
	100% {
		-moz-transform: translateY(0);
	}
}
@-o-keyframes bounceInUp {
	0% {
		opacity: 0;
		-o-transform: translateY(2000px);
	}
	60% {
		opacity: 1;
		-o-transform: translateY(-30px);
	}
	80% {
		-o-transform: translateY(10px);
	}
	100% {
		-o-transform: translateY(0);
	}
}
@keyframes bounceInUp {
	0% {
		opacity: 0;
		transform: translateY(2000px);
	}
	60% {
		opacity: 1;
		transform: translateY(-30px);
	}
	80% {
		transform: translateY(10px);
	}
	100% {
		transform: translateY(0);
	}
}
.bounceInUp {
	-webkit-animation-name: bounceInUp;
	-moz-animation-name: bounceInUp;
	-o-animation-name: bounceInUp;
	animation-name: bounceInUp;
}
@-webkit-keyframes bounceInDown {
	0% {
		opacity: 0;
		-webkit-transform: translateY(-2000px);
	}
	60% {
		opacity: 1;
		-webkit-transform: translateY(30px);
	}
	80% {
		-webkit-transform: translateY(-10px);
	}
	100% {
		-webkit-transform: translateY(0);
	}
}
@-moz-keyframes bounceInDown {
	0% {
		opacity: 0;
		-moz-transform: translateY(-2000px);
	}
	60% {
		opacity: 1;
		-moz-transform: translateY(30px);
	}
	80% {
		-moz-transform: translateY(-10px);
	}
	100% {
		-moz-transform: translateY(0);
	}
}
@-o-keyframes bounceInDown {
	0% {
		opacity: 0;
		-o-transform: translateY(-2000px);
	}
	60% {
		opacity: 1;
		-o-transform: translateY(30px);
	}
	80% {
		-o-transform: translateY(-10px);
	}
	100% {
		-o-transform: translateY(0);
	}
}
@keyframes bounceInDown {
	0% {
		opacity: 0;
		transform: translateY(-2000px);
	}
	60% {
		opacity: 1;
		transform: translateY(30px);
	}
	80% {
		transform: translateY(-10px);
	}
	100% {
		transform: translateY(0);
	}
}
.bounceInDown {
	-webkit-animation-name: bounceInDown;
	-moz-animation-name: bounceInDown;
	-o-animation-name: bounceInDown;
	animation-name: bounceInDown;
}
@-webkit-keyframes bounceInLeft {
	0% {
		opacity: 0;
		-webkit-transform: translateX(-2000px);
	}
	60% {
		opacity: 1;
		-webkit-transform: translateX(30px);
	}
	80% {
		-webkit-transform: translateX(-10px);
	}
	100% {
		-webkit-transform: translateX(0);
	}
}
@-moz-keyframes bounceInLeft {
	0% {
		opacity: 0;
		-moz-transform: translateX(-2000px);
	}
	60% {
		opacity: 1;
		-moz-transform: translateX(30px);
	}
	80% {
		-moz-transform: translateX(-10px);
	}
	100% {
		-moz-transform: translateX(0);
	}
}
@-o-keyframes bounceInLeft {
	0% {
		opacity: 0;
		-o-transform: translateX(-2000px);
	}
	60% {
		opacity: 1;
		-o-transform: translateX(30px);
	}
	80% {
		-o-transform: translateX(-10px);
	}
	100% {
		-o-transform: translateX(0);
	}
}
@keyframes bounceInLeft {
	0% {
		opacity: 0;
		transform: translateX(-2000px);
	}
	60% {
		opacity: 1;
		transform: translateX(30px);
	}
	80% {
		transform: translateX(-10px);
	}
	100% {
		transform: translateX(0);
	}
}
.bounceInLeft {
	-webkit-animation-name: bounceInLeft;
	-moz-animation-name: bounceInLeft;
	-o-animation-name: bounceInLeft;
	animation-name: bounceInLeft;
}
@-webkit-keyframes bounceInRight {
	0% {
		opacity: 0;
		-webkit-transform: translateX(2000px);
	}
	60% {
		opacity: 1;
		-webkit-transform: translateX(-30px);
	}
	80% {
		-webkit-transform: translateX(10px);
	}
	100% {
		-webkit-transform: translateX(0);
	}
}
@-moz-keyframes bounceInRight {
	0% {
		opacity: 0;
		-moz-transform: translateX(2000px);
	}
	60% {
		opacity: 1;
		-moz-transform: translateX(-30px);
	}
	80% {
		-moz-transform: translateX(10px);
	}
	100% {
		-moz-transform: translateX(0);
	}
}
@-o-keyframes bounceInRight {
	0% {
		opacity: 0;
		-o-transform: translateX(2000px);
	}
	60% {
		opacity: 1;
		-o-transform: translateX(-30px);
	}
	80% {
		-o-transform: translateX(10px);
	}
	100% {
		-o-transform: translateX(0);
	}
}
@keyframes bounceInRight {
	0% {
		opacity: 0;
		transform: translateX(2000px);
	}
	60% {
		opacity: 1;
		transform: translateX(-30px);
	}
	80% {
		transform: translateX(10px);
	}
	100% {
		transform: translateX(0);
	}
}
.bounceInRight {
	-webkit-animation-name: bounceInRight;
	-moz-animation-name: bounceInRight;
	-o-animation-name: bounceInRight;
	animation-name: bounceInRight;
}
@-webkit-keyframes bounceOut {
	0% {
		-webkit-transform: scale(1);
	}
	25% {
		-webkit-transform: scale(.95);
	}
	50% {
		opacity: 1;
		-webkit-transform: scale(1.1);
	}
	100% {
		opacity: 0;
		-webkit-transform: scale(.3);
	}	
}
@-moz-keyframes bounceOut {
	0% {
		-moz-transform: scale(1);
	}
	25% {
		-moz-transform: scale(.95);
	}
	50% {
		opacity: 1;
		-moz-transform: scale(1.1);
	}
	100% {
		opacity: 0;
		-moz-transform: scale(.3);
	}	
}
@-o-keyframes bounceOut {
	0% {
		-o-transform: scale(1);
	}
	25% {
		-o-transform: scale(.95);
	}
	50% {
		opacity: 1;
		-o-transform: scale(1.1);
	}
	100% {
		opacity: 0;
		-o-transform: scale(.3);
	}	
}
@keyframes bounceOut {
	0% {
		transform: scale(1);
	}
	25% {
		transform: scale(.95);
	}
	50% {
		opacity: 1;
		transform: scale(1.1);
	}
	100% {
		opacity: 0;
		transform: scale(.3);
	}	
}
.bounceOut {
	-webkit-animation-name: bounceOut;
	-moz-animation-name: bounceOut;
	-o-animation-name: bounceOut;
	animation-name: bounceOut;
}
@-webkit-keyframes bounceOutUp {
	0% {
		-webkit-transform: translateY(0);
	}
	20% {
		opacity: 1;
		-webkit-transform: translateY(20px);
	}
	100% {
		opacity: 0;
		-webkit-transform: translateY(-2000px);
	}
}
@-moz-keyframes bounceOutUp {
	0% {
		-moz-transform: translateY(0);
	}
	20% {
		opacity: 1;
		-moz-transform: translateY(20px);
	}
	100% {
		opacity: 0;
		-moz-transform: translateY(-2000px);
	}
}
@-o-keyframes bounceOutUp {
	0% {
		-o-transform: translateY(0);
	}
	20% {
		opacity: 1;
		-o-transform: translateY(20px);
	}
	100% {
		opacity: 0;
		-o-transform: translateY(-2000px);
	}
}
@keyframes bounceOutUp {
	0% {
		transform: translateY(0);
	}
	20% {
		opacity: 1;
		transform: translateY(20px);
	}
	100% {
		opacity: 0;
		transform: translateY(-2000px);
	}
}
.bounceOutUp {
	-webkit-animation-name: bounceOutUp;
	-moz-animation-name: bounceOutUp;
	-o-animation-name: bounceOutUp;
	animation-name: bounceOutUp;
}
@-webkit-keyframes bounceOutDown {
	0% {
		-webkit-transform: translateY(0);
	}
	20% {
		opacity: 1;
		-webkit-transform: translateY(-20px);
	}
	100% {
		opacity: 0;
		-webkit-transform: translateY(2000px);
	}
}
@-moz-keyframes bounceOutDown {
	0% {
		-moz-transform: translateY(0);
	}
	20% {
		opacity: 1;
		-moz-transform: translateY(-20px);
	}
	100% {
		opacity: 0;
		-moz-transform: translateY(2000px);
	}
}
@-o-keyframes bounceOutDown {
	0% {
		-o-transform: translateY(0);
	}
	20% {
		opacity: 1;
		-o-transform: translateY(-20px);
	}
	100% {
		opacity: 0;
		-o-transform: translateY(2000px);
	}
}
@keyframes bounceOutDown {
	0% {
		transform: translateY(0);
	}
	20% {
		opacity: 1;
		transform: translateY(-20px);
	}
	100% {
		opacity: 0;
		transform: translateY(2000px);
	}
}
.bounceOutDown {
	-webkit-animation-name: bounceOutDown;
	-moz-animation-name: bounceOutDown;
	-o-animation-name: bounceOutDown;
	animation-name: bounceOutDown;
}
@-webkit-keyframes bounceOutLeft {
	0% {
		-webkit-transform: translateX(0);
	}
	20% {
		opacity: 1;
		-webkit-transform: translateX(20px);
	}
	100% {
		opacity: 0;
		-webkit-transform: translateX(-2000px);
	}
}
@-moz-keyframes bounceOutLeft {
	0% {
		-moz-transform: translateX(0);
	}
	20% {
		opacity: 1;
		-moz-transform: translateX(20px);
	}
	100% {
		opacity: 0;
		-moz-transform: translateX(-2000px);
	}
}
@-o-keyframes bounceOutLeft {
	0% {
		-o-transform: translateX(0);
	}
	20% {
		opacity: 1;
		-o-transform: translateX(20px);
	}
	100% {
		opacity: 0;
		-o-transform: translateX(-2000px);
	}
}
@keyframes bounceOutLeft {
	0% {
		transform: translateX(0);
	}
	20% {
		opacity: 1;
		transform: translateX(20px);
	}
	100% {
		opacity: 0;
		transform: translateX(-2000px);
	}
}
.bounceOutLeft {
	-webkit-animation-name: bounceOutLeft;
	-moz-animation-name: bounceOutLeft;
	-o-animation-name: bounceOutLeft;
	animation-name: bounceOutLeft;
}
@-webkit-keyframes bounceOutRight {
	0% {
		-webkit-transform: translateX(0);
	}
	20% {
		opacity: 1;
		-webkit-transform: translateX(-20px);
	}
	100% {
		opacity: 0;
		-webkit-transform: translateX(2000px);
	}
}
@-moz-keyframes bounceOutRight {
	0% {
		-moz-transform: translateX(0);
	}
	20% {
		opacity: 1;
		-moz-transform: translateX(-20px);
	}
	100% {
		opacity: 0;
		-moz-transform: translateX(2000px);
	}
}
@-o-keyframes bounceOutRight {
	0% {
		-o-transform: translateX(0);
	}
	20% {
		opacity: 1;
		-o-transform: translateX(-20px);
	}
	100% {
		opacity: 0;
		-o-transform: translateX(2000px);
	}
}
@keyframes bounceOutRight {
	0% {
		transform: translateX(0);
	}
	20% {
		opacity: 1;
		transform: translateX(-20px);
	}
	100% {
		opacity: 0;
		transform: translateX(2000px);
	}
}
.bounceOutRight {
	-webkit-animation-name: bounceOutRight;
	-moz-animation-name: bounceOutRight;
	-o-animation-name: bounceOutRight;
	animation-name: bounceOutRight;
}
@-webkit-keyframes rotateIn {
	0% {
		-webkit-transform-origin: center center;
		-webkit-transform: rotate(-200deg);
		opacity: 0;
	}
	100% {
		-webkit-transform-origin: center center;
		-webkit-transform: rotate(0);
		opacity: 1;
	}
}
@-moz-keyframes rotateIn {
	0% {
		-moz-transform-origin: center center;
		-moz-transform: rotate(-200deg);
		opacity: 0;
	}
	100% {
		-moz-transform-origin: center center;
		-moz-transform: rotate(0);
		opacity: 1;
	}
}
@-o-keyframes rotateIn {
	0% {
		-o-transform-origin: center center;
		-o-transform: rotate(-200deg);
		opacity: 0;
	}
	100% {
		-o-transform-origin: center center;
		-o-transform: rotate(0);
		opacity: 1;
	}
}
@keyframes rotateIn {
	0% {
		transform-origin: center center;
		transform: rotate(-200deg);
		opacity: 0;
	}
	100% {
		transform-origin: center center;
		transform: rotate(0);
		opacity: 1;
	}
}
.rotateIn {
	-webkit-animation-name: rotateIn;
	-moz-animation-name: rotateIn;
	-o-animation-name: rotateIn;
	animation-name: rotateIn;
}
@-webkit-keyframes rotateInUpLeft {
	0% {
		-webkit-transform-origin: left bottom;
		-webkit-transform: rotate(90deg);
		opacity: 0;
	}
	100% {
		-webkit-transform-origin: left bottom;
		-webkit-transform: rotate(0);
		opacity: 1;
	}
}
@-moz-keyframes rotateInUpLeft {
	0% {
		-moz-transform-origin: left bottom;
		-moz-transform: rotate(90deg);
		opacity: 0;
	}
	100% {
		-moz-transform-origin: left bottom;
		-moz-transform: rotate(0);
		opacity: 1;
	}
}
@-o-keyframes rotateInUpLeft {
	0% {
		-o-transform-origin: left bottom;
		-o-transform: rotate(90deg);
		opacity: 0;
	}
	100% {
		-o-transform-origin: left bottom;
		-o-transform: rotate(0);
		opacity: 1;
	}
}
@keyframes rotateInUpLeft {
	0% {
		transform-origin: left bottom;
		transform: rotate(90deg);
		opacity: 0;
	}
	100% {
		transform-origin: left bottom;
		transform: rotate(0);
		opacity: 1;
	}
}
.rotateInUpLeft {
	-webkit-animation-name: rotateInUpLeft;
	-moz-animation-name: rotateInUpLeft;
	-o-animation-name: rotateInUpLeft;
	animation-name: rotateInUpLeft;
}
@-webkit-keyframes rotateInDownLeft {
	0% {
		-webkit-transform-origin: left bottom;
		-webkit-transform: rotate(-90deg);
		opacity: 0;
	}
	100% {
		-webkit-transform-origin: left bottom;
		-webkit-transform: rotate(0);
		opacity: 1;
	}
}
@-moz-keyframes rotateInDownLeft {
	0% {
		-moz-transform-origin: left bottom;
		-moz-transform: rotate(-90deg);
		opacity: 0;
	}
	100% {
		-moz-transform-origin: left bottom;
		-moz-transform: rotate(0);
		opacity: 1;
	}
}
@-o-keyframes rotateInDownLeft {
	0% {
		-o-transform-origin: left bottom;
		-o-transform: rotate(-90deg);
		opacity: 0;
	}
	100% {
		-o-transform-origin: left bottom;
		-o-transform: rotate(0);
		opacity: 1;
	}
}
@keyframes rotateInDownLeft {
	0% {
		transform-origin: left bottom;
		transform: rotate(-90deg);
		opacity: 0;
	}
	100% {
		transform-origin: left bottom;
		transform: rotate(0);
		opacity: 1;
	}
}
.rotateInDownLeft {
	-webkit-animation-name: rotateInDownLeft;
	-moz-animation-name: rotateInDownLeft;
	-o-animation-name: rotateInDownLeft;
	animation-name: rotateInDownLeft;
}
@-webkit-keyframes rotateInUpRight {
	0% {
		-webkit-transform-origin: right bottom;
		-webkit-transform: rotate(-90deg);
		opacity: 0;
	}
	100% {
		-webkit-transform-origin: right bottom;
		-webkit-transform: rotate(0);
		opacity: 1;
	}
}
@-moz-keyframes rotateInUpRight {
	0% {
		-moz-transform-origin: right bottom;
		-moz-transform: rotate(-90deg);
		opacity: 0;
	}
	100% {
		-moz-transform-origin: right bottom;
		-moz-transform: rotate(0);
		opacity: 1;
	}
}
@-o-keyframes rotateInUpRight {
	0% {
		-o-transform-origin: right bottom;
		-o-transform: rotate(-90deg);
		opacity: 0;
	}
	100% {
		-o-transform-origin: right bottom;
		-o-transform: rotate(0);
		opacity: 1;
	}
}
@keyframes rotateInUpRight {
	0% {
		transform-origin: right bottom;
		transform: rotate(-90deg);
		opacity: 0;
	}
	100% {
		transform-origin: right bottom;
		transform: rotate(0);
		opacity: 1;
	}
}
.rotateInUpRight {
	-webkit-animation-name: rotateInUpRight;
	-moz-animation-name: rotateInUpRight;
	-o-animation-name: rotateInUpRight;
	animation-name: rotateInUpRight;
}
@-webkit-keyframes rotateInDownRight {
	0% {
		-webkit-transform-origin: right bottom;
		-webkit-transform: rotate(90deg);
		opacity: 0;
	}
	100% {
		-webkit-transform-origin: right bottom;
		-webkit-transform: rotate(0);
		opacity: 1;
	}
}
@-moz-keyframes rotateInDownRight {
	0% {
		-moz-transform-origin: right bottom;
		-moz-transform: rotate(90deg);
		opacity: 0;
	}
	100% {
		-moz-transform-origin: right bottom;
		-moz-transform: rotate(0);
		opacity: 1;
	}
}
@-o-keyframes rotateInDownRight {
	0% {
		-o-transform-origin: right bottom;
		-o-transform: rotate(90deg);
		opacity: 0;
	}
	100% {
		-o-transform-origin: right bottom;
		-o-transform: rotate(0);
		opacity: 1;
	}
}
@keyframes rotateInDownRight {
	0% {
		transform-origin: right bottom;
		transform: rotate(90deg);
		opacity: 0;
	}
	100% {
		transform-origin: right bottom;
		transform: rotate(0);
		opacity: 1;
	}
}
.rotateInDownRight {
	-webkit-animation-name: rotateInDownRight;
	-moz-animation-name: rotateInDownRight;
	-o-animation-name: rotateInDownRight;
	animation-name: rotateInDownRight;
}
@-webkit-keyframes rotateOut {
	0% {
		-webkit-transform-origin: center center;
		-webkit-transform: rotate(0);
		opacity: 1;
	}
	100% {
		-webkit-transform-origin: center center;
		-webkit-transform: rotate(200deg);
		opacity: 0;
	}
}
@-moz-keyframes rotateOut {
	0% {
		-moz-transform-origin: center center;
		-moz-transform: rotate(0);
		opacity: 1;
	}
	100% {
		-moz-transform-origin: center center;
		-moz-transform: rotate(200deg);
		opacity: 0;
	}
}
@-o-keyframes rotateOut {
	0% {
		-o-transform-origin: center center;
		-o-transform: rotate(0);
		opacity: 1;
	}
	100% {
		-o-transform-origin: center center;
		-o-transform: rotate(200deg);
		opacity: 0;
	}
}
@keyframes rotateOut {
	0% {
		transform-origin: center center;
		transform: rotate(0);
		opacity: 1;
	}
	100% {
		transform-origin: center center;
		transform: rotate(200deg);
		opacity: 0;
	}
}
.rotateOut {
	-webkit-animation-name: rotateOut;
	-moz-animation-name: rotateOut;
	-o-animation-name: rotateOut;
	animation-name: rotateOut;
}
@-webkit-keyframes rotateOutUpLeft {
	0% {
		-webkit-transform-origin: left bottom;
		-webkit-transform: rotate(0);
		opacity: 1;
	}
	100% {
		-webkit-transform-origin: left bottom;
		-webkit-transform: rotate(-90deg);
		opacity: 0;
	}
}
@-moz-keyframes rotateOutUpLeft {
	0% {
		-moz-transform-origin: left bottom;
		-moz-transform: rotate(0);
		opacity: 1;
	}
	100% {
		-moz-transform-origin: left bottom;
		-moz-transform: rotate(-90deg);
		opacity: 0;
	}
}
@-o-keyframes rotateOutUpLeft {
	0% {
		-o-transform-origin: left bottom;
		-o-transform: rotate(0);
		opacity: 1;
	}
	100% {
		-o-transform-origin: left bottom;
		-o-transform: rotate(-90deg);
		opacity: 0;
	}
}
@keyframes rotateOutUpLeft {
	0% {
		transform-origin: left bottom;
		transform: rotate(0);
		opacity: 1;
	}
	100% {
		-transform-origin: left bottom;
		-transform: rotate(-90deg);
		opacity: 0;
	}
}
.rotateOutUpLeft {
	-webkit-animation-name: rotateOutUpLeft;
	-moz-animation-name: rotateOutUpLeft;
	-o-animation-name: rotateOutUpLeft;
	animation-name: rotateOutUpLeft;
}
@-webkit-keyframes rotateOutDownLeft {
	0% {
		-webkit-transform-origin: left bottom;
		-webkit-transform: rotate(0);
		opacity: 1;
	}
	100% {
		-webkit-transform-origin: left bottom;
		-webkit-transform: rotate(90deg);
		opacity: 0;
	}
}
@-moz-keyframes rotateOutDownLeft {
	0% {
		-moz-transform-origin: left bottom;
		-moz-transform: rotate(0);
		opacity: 1;
	}
	100% {
		-moz-transform-origin: left bottom;
		-moz-transform: rotate(90deg);
		opacity: 0;
	}
}
@-o-keyframes rotateOutDownLeft {
	0% {
		-o-transform-origin: left bottom;
		-o-transform: rotate(0);
		opacity: 1;
	}
	100% {
		-o-transform-origin: left bottom;
		-o-transform: rotate(90deg);
		opacity: 0;
	}
}
@keyframes rotateOutDownLeft {
	0% {
		transform-origin: left bottom;
		transform: rotate(0);
		opacity: 1;
	}
	100% {
		transform-origin: left bottom;
		transform: rotate(90deg);
		opacity: 0;
	}
}
.rotateOutDownLeft {
	-webkit-animation-name: rotateOutDownLeft;
	-moz-animation-name: rotateOutDownLeft;
	-o-animation-name: rotateOutDownLeft;
	animation-name: rotateOutDownLeft;
}
@-webkit-keyframes rotateOutUpRight {
	0% {
		-webkit-transform-origin: right bottom;
		-webkit-transform: rotate(0);
		opacity: 1;
	}
	100% {
		-webkit-transform-origin: right bottom;
		-webkit-transform: rotate(90deg);
		opacity: 0;
	}
}
@-moz-keyframes rotateOutUpRight {
	0% {
		-moz-transform-origin: right bottom;
		-moz-transform: rotate(0);
		opacity: 1;
	}
	100% {
		-moz-transform-origin: right bottom;
		-moz-transform: rotate(90deg);
		opacity: 0;
	}
}
@-o-keyframes rotateOutUpRight {
	0% {
		-o-transform-origin: right bottom;
		-o-transform: rotate(0);
		opacity: 1;
	}
	100% {
		-o-transform-origin: right bottom;
		-o-transform: rotate(90deg);
		opacity: 0;
	}
}
@keyframes rotateOutUpRight {
	0% {
		transform-origin: right bottom;
		transform: rotate(0);
		opacity: 1;
	}
	100% {
		transform-origin: right bottom;
		transform: rotate(90deg);
		opacity: 0;
	}
}
.rotateOutUpRight {
	-webkit-animation-name: rotateOutUpRight;
	-moz-animation-name: rotateOutUpRight;
	-o-animation-name: rotateOutUpRight;
	animation-name: rotateOutUpRight;
}
@-webkit-keyframes rotateOutDownRight {
	0% {
		-webkit-transform-origin: right bottom;
		-webkit-transform: rotate(0);
		opacity: 1;
	}
	100% {
		-webkit-transform-origin: right bottom;
		-webkit-transform: rotate(-90deg);
		opacity: 0;
	}
}
@-moz-keyframes rotateOutDownRight {
	0% {
		-moz-transform-origin: right bottom;
		-moz-transform: rotate(0);
		opacity: 1;
	}
	100% {
		-moz-transform-origin: right bottom;
		-moz-transform: rotate(-90deg);
		opacity: 0;
	}
}
@-o-keyframes rotateOutDownRight {
	0% {
		-o-transform-origin: right bottom;
		-o-transform: rotate(0);
		opacity: 1;
	}
	100% {
		-o-transform-origin: right bottom;
		-o-transform: rotate(-90deg);
		opacity: 0;
	}
}
@keyframes rotateOutDownRight {
	0% {
		transform-origin: right bottom;
		transform: rotate(0);
		opacity: 1;
	}
	100% {
		transform-origin: right bottom;
		transform: rotate(-90deg);
		opacity: 0;
	}
}
.rotateOutDownRight {
	-webkit-animation-name: rotateOutDownRight;
	-moz-animation-name: rotateOutDownRight;
	-o-animation-name: rotateOutDownRight;
	animation-name: rotateOutDownRight;
}
@-webkit-keyframes lightSpeedIn {
	0% { -webkit-transform: translateX(100%) skewX(-30deg); opacity: 0; }
	60% { -webkit-transform: translateX(-20%) skewX(30deg); opacity: 1; }
	80% { -webkit-transform: translateX(0%) skewX(-15deg); opacity: 1; }
	100% { -webkit-transform: translateX(0%) skewX(0deg); opacity: 1; }
}
@-moz-keyframes lightSpeedIn {
	0% { -moz-transform: translateX(100%) skewX(-30deg); opacity: 0; }
	60% { -moz-transform: translateX(-20%) skewX(30deg); opacity: 1; }
	80% { -moz-transform: translateX(0%) skewX(-15deg); opacity: 1; }
	100% { -moz-transform: translateX(0%) skewX(0deg); opacity: 1; }
}
@-o-keyframes lightSpeedIn {
	0% { -o-transform: translateX(100%) skewX(-30deg); opacity: 0; }
	60% { -o-transform: translateX(-20%) skewX(30deg); opacity: 1; }
	80% { -o-transform: translateX(0%) skewX(-15deg); opacity: 1; }
	100% { -o-transform: translateX(0%) skewX(0deg); opacity: 1; }
}
@keyframes lightSpeedIn {
	0% { transform: translateX(100%) skewX(-30deg); opacity: 0; }
	60% { transform: translateX(-20%) skewX(30deg); opacity: 1; }
	80% { transform: translateX(0%) skewX(-15deg); opacity: 1; }
	100% { transform: translateX(0%) skewX(0deg); opacity: 1; }
}
.lightSpeedIn {
    -webkit-animation-name: lightSpeedIn;
    -moz-animation-name: lightSpeedIn;
    -o-animation-name: lightSpeedIn;
    animation-name: lightSpeedIn;
    -webkit-animation-timing-function: ease-out;
    -moz-animation-timing-function: ease-out;
    -o-animation-timing-function: ease-out;
    animation-timing-function: ease-out;
}
@-webkit-keyframes lightSpeedOut {
    0% { -webkit-transform: translateX(0%) skewX(0deg); opacity: 1; }
	100% { -webkit-transform: translateX(100%) skewX(-30deg); opacity: 0; }
}
@-moz-keyframes lightSpeedOut {
	0% { -moz-transform: translateX(0%) skewX(0deg); opacity: 1; }
	100% { -moz-transform: translateX(100%) skewX(-30deg); opacity: 0; }
}
@-o-keyframes lightSpeedOut {
	0% { -o-transform: translateX(0%) skewX(0deg); opacity: 1; }
	100% { -o-transform: translateX(100%) skewX(-30deg); opacity: 0; }
}
@keyframes lightSpeedOut {
	0% { transform: translateX(0%) skewX(0deg); opacity: 1; }
	100% { transform: translateX(100%) skewX(-30deg); opacity: 0; }
}
.lightSpeedOut {
    -webkit-animation-name: lightSpeedOut;
    -moz-animation-name: lightSpeedOut;
    -o-animation-name: lightSpeedOut;
    animation-name: lightSpeedOut;
    -webkit-animation-timing-function: ease-in;
    -moz-animation-timing-function: ease-in;
    -o-animation-timing-function: ease-in;
    animation-timing-function: ease-in;
}
@-webkit-keyframes hinge {
	0% { -webkit-transform: rotate(0); -webkit-transform-origin: top left; -webkit-animation-timing-function: ease-in-out; }	
	20%, 60% { -webkit-transform: rotate(80deg); -webkit-transform-origin: top left; -webkit-animation-timing-function: ease-in-out; }	
	40% { -webkit-transform: rotate(60deg); -webkit-transform-origin: top left; -webkit-animation-timing-function: ease-in-out; }	
	80% { -webkit-transform: rotate(60deg) translateY(0); opacity: 1; -webkit-transform-origin: top left; -webkit-animation-timing-function: ease-in-out; }	
	100% { -webkit-transform: translateY(700px); opacity: 0; }
}
@-moz-keyframes hinge {
	0% { -moz-transform: rotate(0); -moz-transform-origin: top left; -moz-animation-timing-function: ease-in-out; }	
	20%, 60% { -moz-transform: rotate(80deg); -moz-transform-origin: top left; -moz-animation-timing-function: ease-in-out; }	
	40% { -moz-transform: rotate(60deg); -moz-transform-origin: top left; -moz-animation-timing-function: ease-in-out; }	
	80% { -moz-transform: rotate(60deg) translateY(0); opacity: 1; -moz-transform-origin: top left; -moz-animation-timing-function: ease-in-out; }	
	100% { -moz-transform: translateY(700px); opacity: 0; }
}
@-o-keyframes hinge {
	0% { -o-transform: rotate(0); -o-transform-origin: top left; -o-animation-timing-function: ease-in-out; }	
	20%, 60% { -o-transform: rotate(80deg); -o-transform-origin: top left; -o-animation-timing-function: ease-in-out; }	
	40% { -o-transform: rotate(60deg); -o-transform-origin: top left; -o-animation-timing-function: ease-in-out; }	
	80% { -o-transform: rotate(60deg) translateY(0); opacity: 1; -o-transform-origin: top left; -o-animation-timing-function: ease-in-out; }	
	100% { -o-transform: translateY(700px); opacity: 0; }
}
@keyframes hinge {
	0% { transform: rotate(0); transform-origin: top left; animation-timing-function: ease-in-out; }	
	20%, 60% { transform: rotate(80deg); transform-origin: top left; animation-timing-function: ease-in-out; }	
	40% { transform: rotate(60deg); transform-origin: top left; animation-timing-function: ease-in-out; }	
	80% { transform: rotate(60deg) translateY(0); opacity: 1; transform-origin: top left; animation-timing-function: ease-in-out; }	
	100% { transform: translateY(700px); opacity: 0; }
}
.hinge {
	-webkit-animation-name: hinge;
	-moz-animation-name: hinge;
	-o-animation-name: hinge;
	animation-name: hinge;
}
/* originally authored by Nick Pettit - https://github.com/nickpettit/glide */
@-webkit-keyframes rollIn {
	0% { opacity: 0; -webkit-transform: translateX(-100%) rotate(-120deg); }
	100% { opacity: 1; -webkit-transform: translateX(0px) rotate(0deg); }
}
@-moz-keyframes rollIn {
	0% { opacity: 0; -moz-transform: translateX(-100%) rotate(-120deg); }
	100% { opacity: 1; -moz-transform: translateX(0px) rotate(0deg); }
}
@-o-keyframes rollIn {
	0% { opacity: 0; -o-transform: translateX(-100%) rotate(-120deg); }
	100% { opacity: 1; -o-transform: translateX(0px) rotate(0deg); }
}
@keyframes rollIn {
	0% { opacity: 0; transform: translateX(-100%) rotate(-120deg); }
	100% { opacity: 1; transform: translateX(0px) rotate(0deg); }
}
.rollIn {
	-webkit-animation-name: rollIn;
	-moz-animation-name: rollIn;
	-o-animation-name: rollIn;
	animation-name: rollIn;
}
/* originally authored by Nick Pettit - https://github.com/nickpettit/glide */
@-webkit-keyframes rollOut {
    0% {
		opacity: 1;
		-webkit-transform: translateX(0px) rotate(0deg);
	}
    100% {
		opacity: 0;
		-webkit-transform: translateX(100%) rotate(120deg);
	}
}
@-moz-keyframes rollOut {
    0% {
		opacity: 1;
		-moz-transform: translateX(0px) rotate(0deg);
	}
    100% {
		opacity: 0;
		-moz-transform: translateX(100%) rotate(120deg);
	}
}
@-o-keyframes rollOut {
    0% {
		opacity: 1;
		-o-transform: translateX(0px) rotate(0deg);
	}
    100% {
		opacity: 0;
		-o-transform: translateX(100%) rotate(120deg);
	}
}
@keyframes rollOut {
    0% {
		opacity: 1;
		transform: translateX(0px) rotate(0deg);
	}
    100% {
		opacity: 0;
		transform: translateX(100%) rotate(120deg);
	}
}
.rollOut {
	-webkit-animation-name: rollOut;
	-moz-animation-name: rollOut;
	-o-animation-name: rollOut;
	animation-name: rollOut;
}
================================================

File: awesome-bootstrap-checkbox.css
================================================
.checkbox {
  padding-left: 20px;
}
.checkbox label {
  display: inline-block;
  vertical-align: middle;
  position: relative;
  padding-left: 5px;
}
.checkbox label::before {
  content: "";
  display: inline-block;
  position: absolute;
  width: 17px;
  height: 17px;
  left: 0;
  margin-left: -20px;
  border: 1px solid #cccccc;
  border-radius: 3px;
  background-color: #fff;
  -webkit-transition: border 0.15s ease-in-out, color 0.15s ease-in-out;
  -o-transition: border 0.15s ease-in-out, color 0.15s ease-in-out;
  transition: border 0.15s ease-in-out, color 0.15s ease-in-out;
}
.checkbox label::after {
  display: inline-block;
  position: absolute;
  width: 16px;
  height: 16px;
  left: 0;
  top: 0;
  margin-left: -20px;
  padding-left: 3px;
  padding-top: 1px;
  font-size: 11px;
  color: #555555;
}
.checkbox input[type="checkbox"],
.checkbox input[type="radio"] {
  opacity: 0;
  z-index: 1;
}
.checkbox input[type="checkbox"]:focus + label::before,
.checkbox input[type="radio"]:focus + label::before {
  outline: thin dotted;
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
.checkbox input[type="checkbox"]:checked + label::after,
.checkbox input[type="radio"]:checked + label::after {
  font-family: "FontAwesome";
  content: "\f00c";
}
.checkbox input[type="checkbox"]:indeterminate + label::after,
.checkbox input[type="radio"]:indeterminate + label::after {
  display: block;
  content: "";
  width: 10px;
  height: 3px;
  background-color: #555555;
  border-radius: 2px;
  margin-left: -16.5px;
  margin-top: 7px;
}
.checkbox input[type="checkbox"]:disabled + label,
.checkbox input[type="radio"]:disabled + label {
  opacity: 0.65;
}
.checkbox input[type="checkbox"]:disabled + label::before,
.checkbox input[type="radio"]:disabled + label::before {
  background-color: #eeeeee;
  cursor: not-allowed;
}
.checkbox.checkbox-circle label::before {
  border-radius: 50%;
}
.checkbox.checkbox-inline {
  margin-top: 0;
}
.checkbox-primary input[type="checkbox"]:checked + label::before,
.checkbox-primary input[type="radio"]:checked + label::before {
  background-color: #337ab7;
  border-color: #337ab7;
}
.checkbox-primary input[type="checkbox"]:checked + label::after,
.checkbox-primary input[type="radio"]:checked + label::after {
  color: #fff;
}
.checkbox-danger input[type="checkbox"]:checked + label::before,
.checkbox-danger input[type="radio"]:checked + label::before {
  background-color: #d9534f;
  border-color: #d9534f;
}
.checkbox-danger input[type="checkbox"]:checked + label::after,
.checkbox-danger input[type="radio"]:checked + label::after {
  color: #fff;
}
.checkbox-info input[type="checkbox"]:checked + label::before,
.checkbox-info input[type="radio"]:checked + label::before {
  background-color: #5bc0de;
  border-color: #5bc0de;
}
.checkbox-info input[type="checkbox"]:checked + label::after,
.checkbox-info input[type="radio"]:checked + label::after {
  color: #fff;
}
.checkbox-warning input[type="checkbox"]:checked + label::before,
.checkbox-warning input[type="radio"]:checked + label::before {
  background-color: #f0ad4e;
  border-color: #f0ad4e;
}
.checkbox-warning input[type="checkbox"]:checked + label::after,
.checkbox-warning input[type="radio"]:checked + label::after {
  color: #fff;
}
.checkbox-success input[type="checkbox"]:checked + label::before,
.checkbox-success input[type="radio"]:checked + label::before {
  background-color: #5cb85c;
  border-color: #5cb85c;
}
.checkbox-success input[type="checkbox"]:checked + label::after,
.checkbox-success input[type="radio"]:checked + label::after {
  color: #fff;
}
.checkbox-primary input[type="checkbox"]:indeterminate + label::before,
.checkbox-primary input[type="radio"]:indeterminate + label::before {
  background-color: #337ab7;
  border-color: #337ab7;
}
.checkbox-primary input[type="checkbox"]:indeterminate + label::after,
.checkbox-primary input[type="radio"]:indeterminate + label::after {
  background-color: #fff;
}
.checkbox-danger input[type="checkbox"]:indeterminate + label::before,
.checkbox-danger input[type="radio"]:indeterminate + label::before {
  background-color: #d9534f;
  border-color: #d9534f;
}
.checkbox-danger input[type="checkbox"]:indeterminate + label::after,
.checkbox-danger input[type="radio"]:indeterminate + label::after {
  background-color: #fff;
}
.checkbox-info input[type="checkbox"]:indeterminate + label::before,
.checkbox-info input[type="radio"]:indeterminate + label::before {
  background-color: #5bc0de;
  border-color: #5bc0de;
}
.checkbox-info input[type="checkbox"]:indeterminate + label::after,
.checkbox-info input[type="radio"]:indeterminate + label::after {
  background-color: #fff;
}
.checkbox-warning input[type="checkbox"]:indeterminate + label::before,
.checkbox-warning input[type="radio"]:indeterminate + label::before {
  background-color: #f0ad4e;
  border-color: #f0ad4e;
}
.checkbox-warning input[type="checkbox"]:indeterminate + label::after,
.checkbox-warning input[type="radio"]:indeterminate + label::after {
  background-color: #fff;
}
.checkbox-success input[type="checkbox"]:indeterminate + label::before,
.checkbox-success input[type="radio"]:indeterminate + label::before {
  background-color: #5cb85c;
  border-color: #5cb85c;
}
.checkbox-success input[type="checkbox"]:indeterminate + label::after,
.checkbox-success input[type="radio"]:indeterminate + label::after {
  background-color: #fff;
}
.radio {
  padding-left: 20px;
}
.radio label {
  display: inline-block;
  vertical-align: middle;
  position: relative;
  padding-left: 5px;
}
.radio label::before {
  content: "";
  display: inline-block;
  position: absolute;
  width: 17px;
  height: 17px;
  left: 0;
  margin-left: -20px;
  border: 1px solid #cccccc;
  border-radius: 50%;
  background-color: #fff;
  -webkit-transition: border 0.15s ease-in-out;
  -o-transition: border 0.15s ease-in-out;
  transition: border 0.15s ease-in-out;
}
.radio label::after {
  display: inline-block;
  position: absolute;
  content: " ";
  width: 11px;
  height: 11px;
  left: 3px;
  top: 3px;
  margin-left: -20px;
  border-radius: 50%;
  background-color: #555555;
  -webkit-transform: scale(0, 0);
  -ms-transform: scale(0, 0);
  -o-transform: scale(0, 0);
  transform: scale(0, 0);
  -webkit-transition: -webkit-transform 0.1s cubic-bezier(0.8, -0.33, 0.2, 1.33);
  -moz-transition: -moz-transform 0.1s cubic-bezier(0.8, -0.33, 0.2, 1.33);
  -o-transition: -o-transform 0.1s cubic-bezier(0.8, -0.33, 0.2, 1.33);
  transition: transform 0.1s cubic-bezier(0.8, -0.33, 0.2, 1.33);
}
.radio input[type="radio"] {
  opacity: 0;
  z-index: 1;
}
.radio input[type="radio"]:focus + label::before {
  outline: thin dotted;
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
.radio input[type="radio"]:checked + label::after {
  -webkit-transform: scale(1, 1);
  -ms-transform: scale(1, 1);
  -o-transform: scale(1, 1);
  transform: scale(1, 1);
}
.radio input[type="radio"]:disabled + label {
  opacity: 0.65;
}
.radio input[type="radio"]:disabled + label::before {
  cursor: not-allowed;
}
.radio.radio-inline {
  margin-top: 0;
}
.radio-primary input[type="radio"] + label::after {
  background-color: #337ab7;
}
.radio-primary input[type="radio"]:checked + label::before {
  border-color: #337ab7;
}
.radio-primary input[type="radio"]:checked + label::after {
  background-color: #337ab7;
}
.radio-danger input[type="radio"] + label::after {
  background-color: #d9534f;
}
.radio-danger input[type="radio"]:checked + label::before {
  border-color: #d9534f;
}
.radio-danger input[type="radio"]:checked + label::after {
  background-color: #d9534f;
}
.radio-info input[type="radio"] + label::after {
  background-color: #5bc0de;
}
.radio-info input[type="radio"]:checked + label::before {
  border-color: #5bc0de;
}
.radio-info input[type="radio"]:checked + label::after {
  background-color: #5bc0de;
}
.radio-warning input[type="radio"] + label::after {
  background-color: #f0ad4e;
}
.radio-warning input[type="radio"]:checked + label::before {
  border-color: #f0ad4e;
}
.radio-warning input[type="radio"]:checked + label::after {
  background-color: #f0ad4e;
}
.radio-success input[type="radio"] + label::after {
  background-color: #5cb85c;
}
.radio-success input[type="radio"]:checked + label::before {
  border-color: #5cb85c;
}
.radio-success input[type="radio"]:checked + label::after {
  background-color: #5cb85c;
}
input[type="checkbox"].styled:checked + label:after,
input[type="radio"].styled:checked + label:after {
  font-family: 'FontAwesome';
  content: "\f00c";
}
input[type="checkbox"] .styled:checked + label::before,
input[type="radio"] .styled:checked + label::before {
  color: #fff;
}
input[type="checkbox"] .styled:checked + label::after,
input[type="radio"] .styled:checked + label::after {
  color: #fff;
}
================================================

File: customModal.css
================================================
.custom-modal {
    display: none;
    position: fixed;
    z-index: 1053;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: auto;
    background-color: rgb(0,0,0);
    background-color: rgba(0,0,0,0.5);
}
.cmodal-content {
    position: relative;
    margin: 10% auto;
    border: 1px solid #888;
    border-radius: 10px;
    width: 40%;
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2),0 6px 20px 0 rgba(0,0,0,0.19);
    -webkit-animation: cmodalmove .4s ;
    -o-animation: cmodalmove .4s;
    -moz-animation: cmodalmove .4s;
    animation: cmodalmove .4s;
}
@-webkit-keyframes cmodalmove {
    0%   {top:-400px;}
    100% {top:0px;}
}
@keyframes cmodalmove {
    0%   {top:-400px;}
    100% {top:0px;}
}
.cmodal-header {
    display: block;
    height: fit-content;
    width: 100%;
    border-radius: 10px 10px 0px 0px;
    background-color: rgb(0,0,0);
    background-color: rgba(0,0,0,0.25);
    color: white;
    padding: -30px;
}
.cmodal-title {
    font-size: 1.08em;
    display: inline;
    padding: 10px;
    font-weight: 500;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
.cmodal-close:hover {
    background-color: orangered;
}
.cmodal-close {
    float: right;
    height: 100%;
    border-color: rgba(0,0,0,0);
    border-radius: 5px 5px 0px 5px;
    text-align: center;
    font-weight: bold;
    box-shadow: none;
    background: lightgrey;
    cursor: pointer;
}
.cmodal-body {
    display: inline;
}
.cmodal-message {
    display: block;
    padding: 20px 10px;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
.cmodal-icon {
    float: right;
}
.cmodal-footer {
    display: block;
    z-index: -1;
    border-radius: 0px 0px 10px 10px;
    background-color: rgb(255,255,255);
    background-color: rgba(255,255,255,.4);
    text-align: right;
}
.cmodal-button {
    display: inline;
    margin: 3px 3px;
    padding: 3px;
    color: white;
    min-width: 70px;
    cursor: pointer;
    border-radius: 6px;
    border-color: black;
    border-color: rgba(0,0,0,0);
    -webkit-transition: all .2s; 
    -moz-transition: all .2s; 
    transition: all .2s;
    text-decoration: none;
    text-align: center;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
}
.cmodal-button:hover {
    opacity: .95;
    box-shadow: 2px 2px 1px black;
}
.cmodal-ok {
    background: green;
    background:  linear-gradient( green, mediumseagreen);
}
.cmodal-cancel { 
    background: red;
    background: linear-gradient( red, indianred);
}
.cmodal-generic { 
    background: purple;
    background: linear-gradient( purple, mediumpurple);
}
.cmodal-blue {
    background-color: skyblue;
    background: linear-gradient( dodgerblue, deepskyblue);
}
.error {
    background: red;
	background: -moz-linear-gradient(red, indianred);
	background: -webkit-linear-gradient(red, indianred);
	background: -o-linear-gradient(red, indianred);
    background: linear-gradient(red, indianred);
}
.information {
    background: dodgerblue;
	background: -moz-linear-gradient(dodgerblue, lightblue);
	background: -webkit-linear-gradient(dodgerblue, lightblue);
	background: -o-linear-gradient(dodgerblue, lightblue);
    background: linear-gradient(dodgerblue, lightblue);
}
.success {
    background: green;
	background: -moz-linear-gradient(green, mediumseagreen);
	background: -webkit-linear-gradient(green, mediumseagreen);
	background: -o-linear-gradient(green, mediumseagreen);
    background: linear-gradient(green, mediumseagreen);
}
.warning {
    background: darkorange;
	background: -moz-linear-gradient(orangered, darkorange);
	background: -webkit-linear-gradient(orangered, darkorange);
	background: -o-linear-gradient(orangered, darkorange);
    background: linear-gradient(orangered, darkorange);
}
================================================

File: print.css
================================================
.navbar{
display:none;
}
.modal{
	display:none;
}
.action{
	display:none;
}
h1{
	text-transform:uppercase;
}
.title, img {
	display:visible;
}
th{
	text-align:left;
}
td{
	text-align:left;
	border-top:1px solid;
	padding:2px;
}
.btn{
	display:none;
}
.alert{
	display:none;
}
body{
	font-family:arial;
	font-size:13px;
}
.no_print{
	display:none;
}
.printable{
display:visible;
}
span{
text-transform:uppercase;
}
/*
.name span{
display:block;
}
.name span strong{
margin-left:10px;
}
.add_grade{
display:none;
}
.act{
display:none;
}
.logout{
display:none;
}
#add{
display:none;
}
.dataTables_filter{
display:none;
}
.nav{
display:none;
}
.dataTables_paginate {
display:none;
}
#example_length{
display:none;
}
.dataTables_info{
	display:none;
}
*/
================================================

File: style.css
================================================
@import url(http://fonts.googleapis.com/css?family=Open+Sans:400,300,700,600);
@import url(http://fonts.googleapis.com/css?family=Oswald:400,300);
body {
    background: url(../images/bg.jpg);
    background-attachment: fixed;
    background-size: cover;
    background-position: 50% 50%;
    font-family: 'Open Sans', sans-serif;
}
a,
a:hover,
a:focus,
a:active,
a.active {
    outline: 0;
}
ul,ol {
    margin: 0;
    padding: 0;
}
li {
    list-style: none;
}
a {
    color: #FF432E;
    text-decoration: none;
}
a:hover {
    text-decoration: none;
}
p {
    font-family: 'Open Sans', sans-serif;
    font-size: 13px;
    line-height: 21px;
}
/**** Start Logo Section ****/
#logo-section {
}
.logo h1 {
    font-family: 'Lobster', cursive;
    color: #fff;
    font-size: 60px;
}
.logo span {
    color: #999;
}
/**** Start Background Color ****/
.blue {
    background: #28ABE3;
}
.green {
    background: #72bf48;
}
.red {
    background: #FF432E;
}
.olive {
    background: #808000;
}
.purple {
    background: #800080;
}
.fuchsia {
    background: #FF00FF;
}
.navy {
    background: #000080;
}
.bisque {
    background: #FFE4C4;
}
.gold {
    background: #FFD700;
}
.skyblue {
    background: #87CEEB;
}
.lavender {
    background: #E6E6FA;
}
.coral {
    background: #FB7F50; /* wrong code for color */
}
/**** Start Main Body Section ****/
.mainbody-section {
    padding-top: 50px;
    padding-bottom: 30px;
}
.menu-item {
    color: #fff;
    padding-top: 20px;
    padding-bottom: 20px;
    margin-bottom: 30px;
	-webkit-transition: all 0.3s;
	transition: all 0.3s;
}
.menu-item a {
    color: #fff;
    display: block;
	-webkit-transition: all 0.3s;
	transition: all 0.3s;
}
.menu-item a p {
    font-family: 'Oswald', sans-serif;
    font-weight: 300;
    font-size: 20px;
}
.menu-item a i {
    font-size: 50px;
    padding-bottom: 20px;
}
.menu-item:hover a {
    text-decoration: none;
    //color: #333;
	animation: wobble;
	-webkit-animation: wobble;
	animation-duration: 1000ms;
	-webkit-animation-duration: 1000ms;
}
@media only screen 
and (min-width : 600px) 
and (max-width : 991px) {
    .menu-item {
        display: inline-block;
        width: 32.8%;
    }
    .menu-item.responsive {
        width: 49.5%;
        float: left;
        margin-right: 3px;
    }
    .menu-item.responsive-2 {
        width: 49.5%;
        float: right;
    }
}
@media only screen 
and (min-width : 992px) 
and (max-width : 1199px) {
    .menu-item {
        padding-top: 15px;
        padding-bottom: 15px;
    }
    .menu-item a i {
        font-size: 32px;
    }
    .menu-item a p {
        font-size: 16px;
    }
}
/**** Start Modal Section ****/
.modal-content {
	overflow:visible !important;
}
.child-modal .modal-content {
	padding: 50px 0 !important;
	margin-top: 120px !important;
	margin-right: 20px !important;
	margin-left: 20px !important;
	margin-bottom: 80px !important;
	min-height: auto !important;
    border: 2 !important;
    border-radius: 6 !important;
    background-clip: border-box;
    -webkit-box-shadow: none !important;
    -moz-box-shadow: none !important;
    box-shadow: 10px 10px 5px 3px #888888 !important;
    font-weight: 200;
	color: #666 !important;
    font-family: 'Oswald', sans-serif;
    text-transform: none;
}
.modal-footer {
	padding: 1px !important;
}	
table#table-01 {
    width:100%;
	border-radius: 10 !important;
	border-spacing: 5px !important;
}
table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
	border-spacing: 5px !important;
}
th, td {
    padding: 5px;
    text-align: left;
}
table#table-01 tr:nth-child(even) {
    background-color: #eee;
}
table#table-01 tr:nth-child(odd) {
   background-color:#fff;
}
table#table-01 th {
    background-color: black;
    color: white;
}
.card-columns {
 @include media-breakpoint-only(lg) {
    column-count: 4;
  }
  @include media-breakpoint-only(xl) {
    column-count: 5;
  }
 @include media-breakpoint-only(sm) {
    column-count: 3;
 }
	@include media-breakpoint-only(xs) {
    column-count: 3;	
}
}
img.center {
    display: block;
    margin: 0 auto;
}
.center-element {
width: 100%;
margin: 0px auto 0px auto;
}
/*
@media print {
  *,
  *:before,enter code here
  *:after {
    color: #000 !important;
    text-shadow: none !important;
    background: transparent !important;
    -webkit-box-shadow: none !important;
            box-shadow: none !important;
  }
  a,
  a:visited {
    text-decoration: underline;
  }
  a[href]:after {
    content: " (" attr(href) ")";
  }
  abbr[title]:after {
    content: " (" attr(title) ")";
  }
  a[href^="#"]:after,
  a[href^="javascript:"]:after {
    content: "";
  }
  pre,
  blockquote {
    border: 1px solid #999;
    page-break-inside: avoid;
  }
  thead {
    display: table-header-group;
  }
  tr,
  img {
    page-break-inside: avoid;
  }
  img {
    max-width: 100% !important;
  }
  p,
  h2,
  h3 {
    orphans: 3;
    widows: 3;
  }
  h2,
  h3 {
    page-break-after: avoid;
  }
  select {
    background: #fff !important;
  }
  .navbar {
    display: none;
  }
  .btn > .caret,
  .dropup > .btn > .caret {
    border-top-color: #000 !important;
  }
  .label {
    border: 1px solid #000;
  }
  .table {
    border-collapse: collapse !important;
  }
  .table td,
  .table th {
    background-color: #fff !important;
  }
  .table-bordered th,
  .table-bordered td {
    border: 1px solid #ddd !important;
  }
}
*/
================================================

File: dbconfig.php
================================================
<?php
	$DB_host = "localhost";
	$DB_user = "root";
	$DB_pass = "root123";
	$DB_name = "mikrotik";
	try
		{
			$DB_con = new PDO("mysql:host={$DB_host}",$DB_user,$DB_pass);
			$DB_con->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
			$dbname = "`".str_replace("`","``",$DB_name)."`";
			$DB_con->query("CREATE DATABASE IF NOT EXISTS $dbname");
			$DB_con->query("use $dbname");
		}
		catch(PDOException $e) {
			echo "Error: " . $e->getMessage();
	}
	/* Old Version, NOT creating DB if NOT Exist
	$DB_con = new PDO("mysql:host={$DB_host};dbname={$DB_name}",$DB_user,$DB_pass);
	$DB_con->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
	*/
?>
================================================

File: customModal.js
================================================
//Simple redirect function
function redirect_(url) {
    window.location = url;
}
//Determine if a value is present in an array
function is_value_in_array(value, arry) {
    for (var i=0; i<arry.length; i++) {
        if (arry[i] == value){
            return true;
        }
    }
    return false;
}
//Backbone of the modal
//Creates the basic layout and elements of the modal
//This is called by other wrapper function with necessary arguments
function BaseModal (title, message, type, redirect_url,
                    close_on_click, close_on_key, close_keys,
                    buttons) {
    //Actual close function
    var cModalClose = function () {
        cmodal.style.display = "none";
        //Redirect only if URL provided
        if (redirect_url != null) {
            redirect_(redirect_url);
        }
        //Implies the cancel/close button was pressed
        return 0;
    }
    //Close event trigger from other click events
    var cModalCloseTrigger = function (event) {
        if (close_on_click == true) {
            if ((event.target == cmodal) || (event.target == cclose)) {
                cModalClose();
            }
        }
    }
    //Capture keypress and check for exit keys (close_keys)
    var cModalKeypress = function (event) {
        if (close_on_key == true) {
            //Close only if the pressed key was being expected 
            if (is_value_in_array(event.keyCode,close_keys)) {
                cModalClose();
            }
        }
    }
    //Create base modal container div
    var cmodal = document.createElement("div");
    cmodal.className = "custom-modal";
    cmodal.onclick = cModalCloseTrigger;
    //Register keypress event callback
    window.onkeyup = cModalKeypress;
    //Add content div
    var ccontent = document.createElement("div");
    ccontent.className = "cmodal-content " + type;
    cmodal.appendChild(ccontent);
    //Add header div
    var cheader = document.createElement("div");
    cheader.className = "cmodal-header";
    ccontent.appendChild(cheader);
    //Add title-text and close-button;
    //Title text
    var ctitle = document.createElement("span");
    ctitle.className = "cmodal-title";
    ctitle.innerHTML = title;
    //Close button
    var cclose = document.createElement("button");
    cclose.className = "cmodal-close";
    cclose.innerHTML = "x";
    cclose.onclick = cModalClose;
    cheader.appendChild(ctitle);
    cheader.appendChild(cclose);
    //Add modal-body div
    var cbody = document.createElement("div");
    cbody.className = "cmodal-body";
    ccontent.appendChild(cbody);
    //Add message element to the modal body
    var cmessage = document.createElement("span");
    cmessage.className = "cmodal-message";
    cmessage.innerHTML = message;
    cbody.appendChild(cmessage);
    //Add icon after message
    var cicon = document.createElement("img");
    cicon.className = "cmodal-icon"
    cicon.src = "images/"+type+".png";
    cmessage.appendChild(cicon);
    //If this a dialog with buttons, the list "buttons" with
    //the buttons to be added to the modal will be provided
    if (buttons != []) {
        //Create footer 
        var cfooter = document.createElement("div");
        cfooter.className = "cmodal-footer";
        //Populate footer with buttons from the list
        //Set properties of buttons
        for (var i=0; i<buttons.length; i++) {
            var buttn = document.createElement("button");
            buttn.appendChild(document.createTextNode(buttons[i].text));
            buttn.id = i.toString();
            // Default close button
            if (buttons[i].action == "cmodalClose") {
                buttn.onclick = cModalClose;
                buttn.className = "cmodal-button";
                //Style button with default style if not provided
                if ("style" in buttons[i]) {
                    buttn.className = "cmodal-button " + buttons[i].style;
                }
			// JS function
			} else if ((buttons[i].action != "") && (typeof(buttons[i].action) == "function")) {
				buttn.className = "cmodal-button cmodal-ok";
                //The id of this button is its index in "buttons" list
                buttn.onclick = buttons[i].action;
                //Style button with default style if not provided
                if ("style" in buttons[i]) {
                    buttn.className = "cmodal-button " + buttons[i].style;
                }
            // Some URL
            } else if ((buttons[i].action != "") && (typeof(buttons[i].action) != "function")) {
                buttn.className = "cmodal-button cmodal-ok";
                //The id of this button is its index in "buttons" list
                buttn.onclick = function () {
                                redirect_(buttons[this.id].action);
                }
                //Style button with default style if not provided
                if ("style" in buttons[i]) {
                    buttn.className = "cmodal-button " + buttons[i].style;
                }
            // No action was specified. Just return the index of the button pressed
            } else {
                buttn.className = "cmodal-button cmodal-generic";
                buttn.onclick = function () {
                                return this.id;
                }
                //Style button with default style if not provided
                if ("style" in buttons[i]) {
                    buttn.className = "cmodal-button " + buttons[i].style;
                }
            }
            // Append button to the footer
            cfooter.appendChild(buttn);            
        }
        // Add footer to modal content. Happens only if buttons provided
        ccontent.appendChild(cfooter);
    }
    //Enable display of modal
    cmodal.style.display = "block";
    //Append cModal to the document
    document.body.appendChild(cmodal);
    ccontent.focus();
}
//Base modal function call skeleton for reference
//Update this if you change the argument list of BaseModal function
//BaseModal(title, message, type, redirect_url, close_on_click, close_on_key, close_keys, buttons)
//Usual modal dialog
function cmodal (title, message, type, redirect_url=null) {
    return BaseModal(title, message, type, redirect_url, close_on_click=true,
                        close_on_key=true, close_keys=[13,27], buttons=[]);
}
//Modal dialog with buttons
function cmodalOkCancel (title, message, type, buttons=[]) {
    return BaseModal(title, message, type, redirect_url=null, close_on_click=false,
                        close_on_key=true, close_keys=[27,], buttons=buttons);
}
================================================

File: NetworkStream.php
================================================
<?php
/**
 * Wrapper for network stream functionality.
 * 
 * PHP has built in support for various types of network streams, such as HTTP and TCP sockets. One problem that arises with them is the fact that a single fread/fwrite call might not read/write all the data you intended, regardless of whether you're in blocking mode or not. While the PHP manual offers a workaround in the form of a loop with a few variables, using it every single time you want to read/write can be tedious.
This package abstracts this away, so that when you want to get exactly N amount of bytes, you can be sure the upper levels of your app will be dealing with N bytes. Oh, and the functionality is nicely wrapped in an object (but that's just the icing on the cake).
 * 
 * PHP version 5
 * 
 * @category  Net
 * @package   PEAR2_Net_Transmitter
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0a5
 * @link      http://pear2.php.net/PEAR2_Net_Transmitter
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\Transmitter;
/**
 * A network transmitter.
 * 
 * This is a convinience wrapper for network streams. Used to ensure data
 * integrity.
 * 
 * @category Net
 * @package  PEAR2_Net_Transmitter
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_Transmitter
 */
abstract class NetworkStream extends Stream
{
    /**
     * Used in {@link setCrypto()} to disable encryption.
     */
    const CRYPTO_OFF = '';
    /**
     * Used in {@link setCrypto()} to set encryption to either SSLv2 or SSLv3,
     * depending on what the other end supports.
     */
    const CRYPTO_SSL = 'SSLv23';
    /**
     * Used in {@link setCrypto()} to set encryption to SSLv2.
     */
    const CRYPTO_SSL2 = 'SSLv2';
    /**
     * Used in {@link setCrypto()} to set encryption to SSLv3.
     */
    const CRYPTO_SSL3 = 'SSLv3';
    /**
     * Used in {@link setCrypto()} to set encryption to TLS (exact version
     * negotiated between 1.0 and 1.2).
     */
    const CRYPTO_TLS = 'TLS';
    /**
     * @var string The type of stream. Can be either "_CLIENT" or "_SERVER".
     *     Used to complement the encryption type. Must be set by child classes
     *     for {@link setCrypto()} to work properly.
     */
    protected $streamType = '';
    /**
     * @var string The current cryptography setting.
     */
    protected $crypto = '';
    /**
     * Wraps around the specified stream.
     * 
     * @param resource $stream The stream to wrap around.
     */
    public function __construct($stream)
    {
        parent::__construct($stream, true);
    }
    /**
     * Gets the current cryptography setting.
     * 
     * @return string One of this class' CRYPTO_* constants.
     */
    public function getCrypto()
    {
        return $this->crypto;
    }
    /**
     * Sets the current connection's cryptography setting.
     * 
     * @param string $type The encryption type to set. Must be one of this
     *     class' CRYPTO_* constants.
     * 
     * @return boolean TRUE on success, FALSE on failure.
     */
    public function setCrypto($type)
    {
        if (self::CRYPTO_OFF === $type) {
            $result = stream_socket_enable_crypto($this->stream, false);
        } else {
            $result = stream_socket_enable_crypto(
                $this->stream,
                true,
                constant("STREAM_CRYPTO_METHOD_{$type}{$this->streamType}")
            );
        }
        if ($result) {
            $this->crypto = $type;
        }
        return $result;
    }
    /**
     * Checks whether the stream is available for operations.
     * 
     * @return bool TRUE if the stream is available, FALSE otherwise.
     */
    public function isAvailable()
    {
        if (parent::isStream($this->stream)) {
            if ($this->isBlocking && feof($this->stream)) {
                return false;
            }
            $meta = stream_get_meta_data($this->stream);
            return !$meta['eof'];
        }
        return false;
    }
    /**
     * Sets the size of a stream's buffer.
     * 
     * @param int    $size      The desired size of the buffer, in bytes.
     * @param string $direction The buffer of which direction to set. Valid
     *     values are the DIRECTION_* constants.
     * 
     * @return bool TRUE on success, FALSE on failure.
     */
    public function setBuffer($size, $direction = self::DIRECTION_ALL)
    {
        $result = parent::setBuffer($size, $direction);
        if (self::DIRECTION_SEND === $direction
            && function_exists('stream_set_chunk_size') && !$result
        ) {
            return false !== @stream_set_chunk_size($this->stream, $size);
        }
        return $result;
    }
    /**
     * Shutdown a full-duplex connection
     * 
     * Shutdowns (partially or not) a full-duplex connection.
     * 
     * @param string $direction The direction for which to disable further
     *     communications.
     * 
     * @return bool TRUE on success, FALSE on failure.
     */
    public function shutdown($direction = self::DIRECTION_ALL)
    {
        $directionMap = array(
            self::DIRECTION_ALL => STREAM_SHUT_RDWR,
            self::DIRECTION_SEND => STREAM_SHUT_WR,
            self::DIRECTION_RECEIVE => STREAM_SHUT_RD
        );
        return array_key_exists($direction, $directionMap)
            && stream_socket_shutdown($this->stream, $directionMap[$direction]);
    }
}
================================================

File: readme.txt
================================================
Components/Packages/Scripts used in this project
-------------------------------------------------
Elevator  Metro UI Inspired Free Bootstrap HTML5 Template by graygrids.com
https://graygrids.com/item/elevator-metro-ui-inspired-responsive-bootstrap-template/
Twitter Bootstrap (& Jquery) http://getbootstrap.com/, https://jquery.com/
Font Awesome http://fontawesome.io/
Google Fonts http://fonts.googleapis.com/
Pear2 PHP API Client by boenrobot [Vasil Rangelov, a.k.a. boen_robot (boen [dot] robot [at] gmail [dot] com)]
https://github.com/pear2/Net_RouterOS
https://github.com/pear2/Net_RouterOS/wiki
https://wiki.mikrotik.com/wiki/API_PHP_package
http://pear2.php.net/support/
-------------------------------------------------
Developed by: Siby P Varkey, sibyperiyar@gmail.com
Assistance: Sonal Siby, sonusiby@gmail.com
-------------------------------------------------
Visual Documentation at : http://hotspot.zetozone.com
-------------------------------------------------
Software and Hardware
HTML, CSS, JavaScript, PHP, MySql, PDO, Javascript/Ajax, Font Awesome, JQuery, Twitter Bootstrap ... &  PEAR2_Net_RouterOS API are the major software component parts of the utility.  Above all the Mikrotik Router OS Based router or PC working with Router OS configured to an IP is the most important Hardware part involved.  
Requirements: Any web server supports PHP 5.x and all the above.
-------------------------------------------------
Prerequisites
A MySql database need to be created prior to operation, if it doesn't exist will be created automatically on initialization in most cases.
The details of the database need to be updated in the file 'dbconfig.php' file before operation. (Host, DB name, DB Username and DB Password)
The Details of the Router has to be entered in the 'config.php' file before operation, like Host IP, username and password.  If they are not correct or the system is not able to connect to the Hotspot router, will ask for correct credentials in the first screen.
-------------------------------------------------
System Users: Who are operating this utility.
3 User levels: Administrator, Unit Head and System users.
Any number of users can be created by the system Admin.  They can be enabled/disabled, edited, deleted and can reset the password also by the admin. A default system admin with username 'admin' and password 'admin' will be created automatically on initialisation. Admin user can reset passwords of all other users.  On resetting a password, it will be reset to 'password' for that user. All users can change their own password using the change password option available in the system users section.
-------------------------------------------------
Documentation and Help
For more details of the operations and features of the utility please refer the visual documentation available at http://hotspot.zetozone.com
-------------------------------------------------
Major features:
Creation of vouchers for Single person. (Guest User Accounts/Hotspot users)
Creation of vouchers for Multiple persons.
Listing Active Users
Listing inactive Users
Remove Selected/All User Accounts
Remove all validity expired User Accounts
Server Log of Recent Activities
Removal of uninitiated guest accounts.  Accounts created earlier but no one has started using it yet.
Voucher Management and Printing.  6 Different Voucher modes are available for Printing vouchers satisfying the needs of all.
Management of System user Accounts by Admin: Creation, Listing, Activation/Deactivation, Updating details and deletion of System users.
Hotspot User Profiles Management:  Creation/Updation/Deletion of User profiles in the router. Options like Session Timeout, MAC binding of Account, Expiry mode, grace period, price, MAC Cookie Timeout, Keepalive Timeout, Download and Upload Speed Limits, Number of simultaneous user logins allowed per user account etc can be set for each profile.
Re-printing of Last Voucher/Vouchers List.
and many more...
Please visit http://hotspot.zetozone.com for a detailed visual documentation of the project.
-------------------------------------------------
How to Install in different OS based PCs
Linux / Unix variations
................
..................
Windows Based PCs
................
..................
MAC OSX based MACs
................
..................
................
..................
================================================