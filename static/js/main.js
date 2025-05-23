/**
 * JavaScript principal para a aplicação de Móveis Planejados
 *
 * Este arquivo contém todas as funcionalidades JavaScript da aplicação,
 * incluindo o comportamento do menu de navegação, animações e interações.
 */

// Executa quando o documento estiver pronto
$(document).ready(() => {
  // Variáveis para controlar o comportamento do scroll
  let lastScrollTop = 0
  const header = $("#header")
  const scrollThreshold = 50

  /**
   * Função para verificar a posição do scroll e atualizar o header
   *
   * Controla a transparência e visibilidade do header com base na
   * direção do scroll e posição na página.
   */
  function checkScroll() {
    const currentScroll = $(window).scrollTop()

    // Adiciona classe quando o scroll é maior que o threshold
    if (currentScroll > scrollThreshold) {
      header.addClass("scrolled")

      // Verifica a direção do scroll
      if (currentScroll > lastScrollTop) {
        // Scroll para baixo - torna o header transparente
        header.css("background-color", "transparent")
      } else {
        // Scroll para cima - mostra o header com fundo
        header.css("background-color", "var(--primary-color)")
      }
    } else {
      // No topo da página
      header.removeClass("scrolled")
      header.css("background-color", "transparent")
    }

    // Atualiza a última posição de scroll
    lastScrollTop = currentScroll
  }

  // Verifica o scroll no carregamento da página
  checkScroll()

  // Verifica o scroll durante a rolagem
  $(window).scroll(() => {
    checkScroll()
  })

  // Ativa os tooltips do Bootstrap
  const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
  tooltipTriggerList.map((tooltipTriggerEl) => new bootstrap.Tooltip(tooltipTriggerEl))

  // Máscaras para campos de formulário (se a biblioteca jQuery Mask estiver disponível)
  if (typeof $.fn.mask !== "undefined") {
    $(".phone-mask").mask("(00) 00000-0000")
  }

  /**
   * Animação para elementos ao fazer scroll
   *
   * Adiciona a classe 'animated' aos elementos com a classe 'animate-on-scroll'
   * quando eles entram na viewport durante o scroll.
   */
  $(window).scroll(() => {
    $(".animate-on-scroll").each(function () {
      const elementTop = $(this).offset().top
      const elementHeight = $(this).outerHeight()
      const windowHeight = $(window).height()
      const scrollY = $(window).scrollTop()

      // Verifica se o elemento está visível na viewport
      if (scrollY > elementTop - windowHeight + elementHeight / 2) {
        $(this).addClass("animated")
      }
    })
  })

  // Inicializa o scroll para elementos com animação
  $(window).trigger("scroll")
})

// Filtros do catálogo - comportamento melhorado
$(document).ready(() => {
  let filtrosAlterados = false

  // Monitora mudanças nos filtros
  $(".filter-input").change(() => {
    filtrosAlterados = true
    $("#aplicar-filtros").removeClass("btn-primary").addClass("btn-warning")
    $("#aplicar-filtros").html('<i class="fas fa-exclamation-triangle me-2"></i>Aplicar Filtros')
    $("#limpar-filtros").prop("disabled", false)
  })

  // Comportamento do botão limpar filtros
  $("#limpar-filtros").click(function () {
    $(".filter-input").prop("checked", false)
    filtrosAlterados = false
    $("#aplicar-filtros").removeClass("btn-warning").addClass("btn-primary")
    $("#aplicar-filtros").html('<i class="fas fa-filter me-2"></i>Aplicar Filtros')
    $(this).prop("disabled", true)
  })

  // Submissão do formulário
  $("#filtros-form").submit(() => {
    if (!filtrosAlterados && !$(".filter-input:checked").length) {
      return false // Previne submissão se não há filtros selecionados
    }

    // Mostra loading no botão
    $("#aplicar-filtros").html('<i class="fas fa-spinner fa-spin me-2"></i>Aplicando...')
    $("#aplicar-filtros").prop("disabled", true)
  })
})

// Animações para os cards
$(document).ready(() => {
  // Adiciona classe de animação aos cards quando entram na viewport
  function animateCards() {
    $(".categoria-card, .produto-card, .testimonial-card").each(function (index) {
      const card = $(this)
      const cardTop = card.offset().top
      const cardHeight = card.outerHeight()
      const windowHeight = $(window).height()
      const scrollY = $(window).scrollTop()

      if (scrollY > cardTop - windowHeight + cardHeight / 3) {
        setTimeout(() => {
          card.addClass("animate-on-scroll animated")
        }, index * 100) // Delay escalonado para efeito cascata
      }
    })
  }

  // Executa animação no scroll
  $(window).scroll(animateCards)

  // Executa animação no carregamento
  animateCards()
})

// Efeito de hover melhorado para cards
$(document).ready(() => {
  $(".categoria-card, .produto-card").hover(
    function () {
      // Mouse enter
      $(this).find(".btn").addClass("btn-hover-effect")
    },
    function () {
      // Mouse leave
      $(this).find(".btn").removeClass("btn-hover-effect")
    },
  )
})
