using System;
using System.Collections.Generic;
using System.Linq;
using Microsoft.EntityFrameworkCore;
using Microsoft.AspNetCore.Mvc;
using System.Runtime.InteropServices;
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.Hosting;
using Microsoft.AspNetCore.Authentication.Cookies;

namespace Laba
{
    // Моделі для бази даних
    public class Ship
    {
        public int ShipId { get; set; }
        public string Name { get; set; }
        public List<Container> Containers { get; set; }
    }

    public class Port
    {
        public int PortId { get; set; }
        public string Name { get; set; }
        public List<Container> Containers { get; set; }
    }

    public class Container
    {
        public int ContainerId { get; set; }
        public string Name { get; set; }
        public int ShipId { get; set; }
        public int PortId { get; set; }
        public List<Item> Items { get; set; }
    }

    public class Item
    {
        public int ItemId { get; set; }
        public string Name { get; set; }
        public int Count { get; set; }
    }

    // Контекст бази даних
    public class ApplicationDbContext : DbContext
    {
        public DbSet<Ship> Ships { get; set; }
        public DbSet<Port> Ports { get; set; }
        public DbSet<Container> Containers { get; set; }
        public DbSet<Item> Items { get; set; }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            optionsBuilder.UseSqlite("Data Source=database.db");
        }
    }

    // Контролери
    [Route("api/containers")]
    [ApiController]
    public class ContainersController : ControllerBase
    {
        private readonly ApplicationDbContext _context;

        public ContainersController(ApplicationDbContext context)
        {
            _context = context;
        }

        [HttpGet]
        public IActionResult GetContainers()
        {
            var containers = _context.Containers.ToList();
            return Ok(containers);
        }

        [HttpPost]
        public IActionResult CreateContainer(Container container)
        {
            _context.Containers.Add(container);
            _context.SaveChanges();
            return Ok(container);
        }

        [HttpPut("{id}")]
        public IActionResult UpdateContainer(int id, Container updatedContainer)
        {
            var container = _context.Containers.Find(id);
            if (container == null)
            {
                return NotFound();
            }

            container.Name = updatedContainer.Name;
            container.ShipId = updatedContainer.ShipId;
            container.PortId = updatedContainer.PortId;

            _context.SaveChanges();

            return Ok(container);
        }

        [HttpDelete("{id}")]
        public IActionResult DeleteContainer(int id)
        {
            var container = _context.Containers.Find(id);
            if (container == null)
            {
                return NotFound();
            }

            _context.Containers.Remove(container);
            _context.SaveChanges();

            return NoContent();
        }
    }

    [Route("api/items")]
    [ApiController]
    public class ItemsController : ControllerBase
    {
        private readonly ApplicationDbContext _context;

        public ItemsController(ApplicationDbContext context)
        {
            _context = context;
        }

        [HttpGet]
        public IActionResult GetItems()
        {
            var items = _context.Items.ToList();
            return Ok(items);
        }

        [HttpPost]
        public IActionResult CreateItem(Item item)
        {
            _context.Items.Add(item);
            _context.SaveChanges();
            return Ok(item);
        }

        [HttpPut("{id}")]
        public IActionResult UpdateItem(int id, Item updatedItem)
        {
            var item = _context.Items.Find(id);
            if (item == null)
            {
                return NotFound();
            }

            item.Name = updatedItem.Name;
            item.Count = updatedItem.Count;

            _context.SaveChanges();

            return Ok(item);
        }

        [HttpDelete("{id}")]
        public IActionResult DeleteItem(int id)
        {
            var item = _context.Items.Find(id);
            if (item == null)
            {
                return NotFound();
            }

            _context.Items.Remove(item);
            _context.SaveChanges();

            return NoContent();
        }
    }


    public class Startup
    {
        public void ConfigureServices(IServiceCollection services)
        {
            services.AddControllers();

            services.AddDbContext<ApplicationDbContext>(options =>
                options.UseSqlite("Data Source=database.db"));
        }

        public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
        {
            if (env.IsDevelopment())
            {
                app.UseDeveloperExceptionPage();
            }
            else
            {
                app.UseExceptionHandler("/Home/Error");
                app.UseHsts();

            }

            app.UseRouting();

            app.UseEndpoints(endpoints =>
            {
                endpoints.MapControllerRoute(
                    name: "default",
                    pattern: "{controller=Home}/{action=Index}/{id?}");
            });
        }
    }


    public class Program
    {
        public static void Main(string[] args)
        {
            CreateHostBuilder(args).Build().Run();
        }

        public static IHostBuilder CreateHostBuilder(string[] args) =>
            Host.CreateDefaultBuilder(args)
                .ConfigureWebHostDefaults(webBuilder =>
                {
                    webBuilder.UseStartup<Startup>();
                });

        public static void ConfigureServices(IServiceCollection services)
        {
            services.AddDbContext<ApplicationDbContext>(options =>
            options.UseSqlServer("YourConnectionString"));

            services.AddControllers();

            services.AddMemoryCache();


            services.AddAuthentication(CookieAuthenticationDefaults.AuthenticationScheme)
                .AddCookie(options =>
                {
                    options.LoginPath = "/Account/Login";
                    options.LogoutPath = "/Account/Logout";
                });
        }

        public static void Configure(IApplicationBuilder app, IWebHostEnvironment env)
        {
            if (env.IsDevelopment())
            {
                app.UseDeveloperExceptionPage();
            }
            else
            {
                app.UseExceptionHandler("/Home/Error");
                app.UseHsts();
            }

            app.UseRouting();

            app.UseEndpoints(endpoints =>
            {
                endpoints.MapControllerRoute(
                    name: "default",
                    pattern: "{controller=Home}/{action=Index}/{id?}");
            });
        }
    }


}
