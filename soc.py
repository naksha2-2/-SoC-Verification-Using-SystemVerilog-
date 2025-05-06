module testbench;
    // Testbench signals
    reg clk;
    reg reset;
    reg [31:0] data_in;
    wire [31:0] data_out;

    // Instantiate the simple RISC processor
    simple_risc_processor uut (
        .clk(clk),
        .reset(reset),
        .data_in(data_in),
        .data_out(data_out)
    );

    // Clock generation
    always begin
        #5 clk = ~clk;  // Toggle clock every 5 time units
    end

    // Initial block for stimulus
    initial begin
        // Initialize signals
        clk = 0;
        reset = 0;
        data_in = 32'b0;

        // Apply reset
        $display("Applying reset...");
        reset = 1;
        #10 reset = 0;

        // Test case 1: Apply data_in = 5
        data_in = 32'd5;
        #10;
        if (data_out !== 32'd6) $display("Test failed: Expected data_out = 6, got %d", data_out);
        else $display("Test passed: data_out = %d", data_out);

        // Test case 2: Apply data_in = 10
        data_in = 32'd10;
        #10;
        if (data_out !== 32'd11) $display("Test failed: Expected data_out = 11, got %d", data_out);
        else $display("Test passed: data_out = %d", data_out);

        $finish;
    end
endmodule
