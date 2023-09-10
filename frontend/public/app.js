let vm = new Vue({
  el: "#app",
  components: { VoerroTagsInput },
  data: {
    repos: [],
    condition: {
      Lang: "C++",
      Sort: "Name",
      CloneLangs: [],
      Span: "today",
      OnlyNew: true,
    },
  },
  mounted: function () {
    this.load("daily", "C++", "Name");
  },
  watch: {
    condition: {
      handler: function (val, oldVal) {
        this.load(this.getQueryForSpan(val.Span), val.Lang, val.Sort);
      },
      deep: true,
    },
  },
  methods: {
    getQueryForSpan: function (span) {
      switch (span) {
        case "today":
          return "daily";
        case "week":
          return "weekly";
        case "month":
          return "monthly";
        default:
          return "daily";
      }
    },

    load: function (span, lang, sort) {
      fetch(`http://localhost:8000/api/getTrend/${span}/${lang}?format=json`, {
        method: "GET",
      })
        .then((res) => res.json())
        .then((data) => {
          if (sort == "Name") {
            this.repos = data.sort((a, b) => a.Name.localeCompare(b.Name));
          } else if (sort == "All Star") {
            this.repos = data.sort((a, b) => b.Star - a.Star);
          } else if (sort == "Span by Star") {
            this.repos = data.sort((a, b) => b.StarBySpan - a.StarBySpan);
          } else {
            this.repos = data;
          }
        });
    },
  },
});
